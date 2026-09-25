def parentheses_decoder(s):
  open_idx = s.find('(')
  close_idx = s.find(')')
  if open_idx > close_idx:
    return 0
  
  depth_list = []
  while '(' in s:
    s = s.split('(', 1)[1]
    depth = parentheses_decoder(s)
    s = s.split(')', 1)[1]
    depth += 1
    depth_list.append(depth)
  return max(depth_list) if depth_list else 0

print(parentheses_decoder("a()((b(c)d(()))e)"))