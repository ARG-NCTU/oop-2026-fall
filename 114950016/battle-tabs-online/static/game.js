
const SHIP_TYPES = [
  { id:"destroyer", name:"Destroyer", size:2, cooldown:0, description:"被動戰艦，沒有主動技能。" },
  { id:"radar", name:"Radar Ship", size:3, cooldown:3, description:"掃描 3×3 區域，中心格顯示敵艦格數。" },
  { id:"shield", name:"Shield Ship", size:3, cooldown:4, description:"啟動後，下一次命中會轉移到鄰近格。" },
  { id:"missile", name:"Missile Ship", size:4, cooldown:4, description:"十字攻擊中心與上下左右共 5 格。" },
];

const BOARD_SIZE = 10;

let socket = null;
let roomCode = null;
let playerId = null;
let playerIndex = null;
let setupShips = [];
let setupShipIndex = 0;
let direction = "horizontal";
let latestState = null;
let selectedSkill = null;

const screens = {
  lobby: document.getElementById("lobbyScreen"),
  waiting: document.getElementById("waitingScreen"),
  setup: document.getElementById("setupScreen"),
  battle: document.getElementById("battleScreen"),
  gameOver: document.getElementById("gameOverScreen"),
};

function showScreen(name){
  Object.values(screens).forEach(x=>x.classList.add("hidden"));
  screens[name].classList.remove("hidden");
}

function wsUrl(){
  const protocol = location.protocol === "https:" ? "wss" : "ws";
  return `${protocol}://${location.host}/ws`;
}

function connectSocket(onOpen){
  socket = new WebSocket(wsUrl());
  socket.onopen = onOpen;
  socket.onmessage = e => handleMessage(JSON.parse(e.data));
  socket.onclose = () => {
    if(!screens.gameOver.classList.contains("hidden")) return;
    document.getElementById("lobbyStatus").textContent = "連線中斷，請重新整理。";
  };
}

function send(type, payload={}){
  if(socket && socket.readyState === WebSocket.OPEN){
    socket.send(JSON.stringify({type, ...payload}));
  }
}

document.getElementById("createRoomBtn").onclick = () => {
  document.getElementById("lobbyStatus").textContent = "建立房間中...";
  connectSocket(()=>send("create_room"));
};

document.getElementById("joinRoomBtn").onclick = () => {
  const code = document.getElementById("roomCodeInput").value.trim().toUpperCase();
  if(code.length !== 4){
    document.getElementById("lobbyStatus").textContent = "請輸入 4 碼房間代碼。";
    return;
  }
  document.getElementById("lobbyStatus").textContent = "加入房間中...";
  connectSocket(()=>send("join_room",{room_code:code}));
};

function handleMessage(msg){
  if(msg.type === "room_created"){
    roomCode = msg.room_code;
    playerId = msg.player_id;
    playerIndex = msg.player_index;
    document.getElementById("roomCodeDisplay").textContent = roomCode;
    showScreen("waiting");
    return;
  }

  if(msg.type === "joined_room"){
    roomCode = msg.room_code;
    playerId = msg.player_id;
    playerIndex = msg.player_index;
    beginSetup();
    return;
  }

  if(msg.type === "opponent_joined"){
    beginSetup();
    return;
  }

  if(msg.type === "state"){
    latestState = msg.state;
    if(msg.state.phase === "setup"){
      if(!screens.setup.classList.contains("hidden")) {
        document.getElementById("setupStatus").textContent =
          msg.state.both_ready ? "雙方已準備完成" : "等待雙方完成部署";
      }
    }
    if(msg.state.phase === "battle"){
      showScreen("battle");
      renderBattle();
    }
    if(msg.state.phase === "finished"){
      showScreen("gameOver");
      document.getElementById("winnerText").textContent =
        msg.state.you_won ? "你贏了！" : "你輸了";
    }
    return;
  }

  if(msg.type === "error"){
    document.getElementById("lobbyStatus").textContent = msg.message;
    alert(msg.message);
    return;
  }
}

function beginSetup(){
  showScreen("setup");
  document.getElementById("roomCodeTop").textContent = roomCode;
  document.getElementById("playerLabel").textContent = `玩家 ${playerIndex+1}`;
  setupShips = [];
  setupShipIndex = 0;
  renderSetup();
}

function key(row,col){ return `${row},${col}`; }
function inBounds(row,col){ return row>=0&&row<BOARD_SIZE&&col>=0&&col<BOARD_SIZE; }

function renderBoard(container,onClick){
  container.innerHTML = "";
  for(let r=0;r<BOARD_SIZE;r++){
    for(let c=0;c<BOARD_SIZE;c++){
      const cell = document.createElement("button");
      cell.className = "cell";
      cell.dataset.row = r;
      cell.dataset.col = c;
      if(onClick) cell.onclick = ()=>onClick(r,c);
      container.appendChild(cell);
    }
  }
}

function getShipCells(ship,startRow,startCol){
  const cells=[];
  for(let i=0;i<ship.size;i++){
    const r = direction==="vertical" ? startRow+i : startRow;
    const c = direction==="horizontal" ? startCol+i : startCol;
    if(!inBounds(r,c)) return null;
    cells.push(key(r,c));
  }
  return cells;
}

function renderSetup(){
  const board = document.getElementById("setupBoard");
  renderBoard(board,tryPlaceShip);
  const occupied = new Set(setupShips.flatMap(s=>s.cells));
  [...board.children].forEach(cell=>{
    if(occupied.has(key(+cell.dataset.row,+cell.dataset.col))) cell.classList.add("ship");
  });

  const list = document.getElementById("shipList");
  list.innerHTML = "";
  SHIP_TYPES.forEach((ship,i)=>{
    const card = document.createElement("div");
    card.className = "ship-card"+(i===setupShipIndex?" current":"");
    if(i<setupShipIndex) card.style.opacity=".5";
    card.innerHTML = `<strong>${ship.name}</strong><span>長度 ${ship.size}｜${ship.description}</span>`;
    list.appendChild(card);
  });
  document.getElementById("confirmSetupBtn").disabled = setupShipIndex < SHIP_TYPES.length;
}

function tryPlaceShip(row,col){
  if(setupShipIndex>=SHIP_TYPES.length) return;
  const shipType = SHIP_TYPES[setupShipIndex];
  const cells = getShipCells(shipType,row,col);
  if(!cells){ alert("超出戰場範圍"); return; }

  const occupied = new Set(setupShips.flatMap(s=>s.cells));
  if(cells.some(c=>occupied.has(c))){ alert("戰艦不能重疊"); return; }

  setupShips.push({id:shipType.id,cells});
  setupShipIndex++;
  renderSetup();
}

document.getElementById("horizontalBtn").onclick=()=>{
  direction="horizontal";
  document.getElementById("horizontalBtn").classList.add("active");
  document.getElementById("verticalBtn").classList.remove("active");
};
document.getElementById("verticalBtn").onclick=()=>{
  direction="vertical";
  document.getElementById("verticalBtn").classList.add("active");
  document.getElementById("horizontalBtn").classList.remove("active");
};

document.getElementById("confirmSetupBtn").onclick=()=>{
  send("submit_setup",{room_code:roomCode,player_id:playerId,ships:setupShips});
  document.getElementById("confirmSetupBtn").disabled = true;
  document.getElementById("setupStatus").textContent = "已送出部署，等待對手...";
};

function renderBattle(){
  const s = latestState;
  document.getElementById("battleRoomCode").textContent = roomCode;
  document.getElementById("turnText").textContent = s.is_your_turn ? "你的回合" : "對手回合";
  document.getElementById("statusText").textContent = s.message || (s.is_your_turn ? "選擇攻擊格子" : "等待對手行動");

  const own = document.getElementById("ownBoard");
  const enemy = document.getElementById("enemyBoard");
  renderBoard(own,null);
  renderBoard(enemy,(r,c)=>onEnemyClick(r,c));

  const ownShipCells = new Set(s.own_ships.flatMap(x=>x.cells));
  [...own.children].forEach(cell=>{
    const k=key(+cell.dataset.row,+cell.dataset.col);
    if(ownShipCells.has(k)) cell.classList.add("ship");
    const st=s.own_attacks[k];
    if(st==="hit") cell.classList.add("hit");
    if(st==="miss") cell.classList.add("miss");
  });

  [...enemy.children].forEach(cell=>{
    const k=key(+cell.dataset.row,+cell.dataset.col);
    const st=s.enemy_attacks[k];
    if(st==="hit") cell.classList.add("hit");
    if(st==="miss") cell.classList.add("miss");
    if(s.radar_numbers && s.radar_numbers[k] !== undefined){
      cell.classList.add("radar-center");
      cell.textContent=s.radar_numbers[k];
    }
    cell.disabled = !s.is_your_turn;
  });

  renderSkills(s);
}

function renderSkills(s){
  const list=document.getElementById("skillList");
  list.innerHTML="";
  s.own_ships.forEach(ship=>{
    const def=SHIP_TYPES.find(x=>x.id===ship.id);
    const card=document.createElement("div");
    card.className="skill-card";
    card.innerHTML=`<strong>${def.name}${ship.sunk?"（已沉沒）":""}</strong><span>${def.description}</span>`;

    const btn=document.createElement("button");
    btn.className="skill-btn";
    let disabled = !s.is_your_turn || ship.sunk || ship.id==="destroyer" || ship.cooldown_remaining>0;
    btn.disabled=disabled;

    if(ship.id==="destroyer") btn.textContent="被動";
    else if(ship.cooldown_remaining>0) btn.textContent=`冷卻 ${ship.cooldown_remaining} 回合`;
    else btn.textContent="使用技能";

    if(!disabled){
      btn.onclick=()=>{
        if(ship.id==="shield"){
          send("use_skill",{room_code:roomCode,player_id:playerId,skill:"shield"});
        }else{
          selectedSkill=ship.id;
          document.getElementById("statusText").textContent=`已選擇 ${def.name}，請點敵方格子`;
          renderSkills(s);
        }
      };
    }
    if(selectedSkill===ship.id) btn.classList.add("active");
    card.appendChild(btn);
    list.appendChild(card);
  });
}

function onEnemyClick(row,col){
  if(!latestState || !latestState.is_your_turn) return;
  if(selectedSkill){
    send("use_skill",{room_code:roomCode,player_id:playerId,skill:selectedSkill,row,col});
    selectedSkill=null;
  }else{
    send("attack",{room_code:roomCode,player_id:playerId,row,col});
  }
}

document.getElementById("backLobbyBtn").onclick=()=>location.reload();
