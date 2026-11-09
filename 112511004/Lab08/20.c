bool isValid(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return true;
    if (n % 2 != 0) return false;

    char* stack = malloc(n * sizeof(char));
    if (stack == NULL) return false;

    int top = 0;

    for (int i = 0; i < n; i++) {
        char c = s[i];

        if (c == '(' || c == '[' || c == '{') {
            stack[top] = c;
            top++;
        } 
        else {
            if (top == 0) {
                free(stack);
                return false;
            }
            char left = stack[top - 1];

            if ((c == ')' && left != '(') || (c == ']' && left != '[') ||  (c == '}' && left != '{')) {
                free(stack);
                return false;
            }
            top--;
        }
    }

    free(stack);
    return top == 0;
}