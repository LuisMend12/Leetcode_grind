// Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

// If there exist multiple answers, you can return any of them.

 

int *a;
int *b;
int len;
int i;
char *m;

struct TreeNode* dfs() {
    struct TreeNode *n = (struct TreeNode*)calloc(1, sizeof(struct TreeNode));
    n->val = a[i];
    const int j = m[a[i++]]; // postorder index
    const int r = j != 0 ? b[j - 1] : -1; // right child
    b[j] = -1; // del node from postorder
    if (r != -1) {
        n->left = dfs();
        if (i < len && r == a[i]) {
            n->right = dfs();
        }
    }
    return n;
}

struct TreeNode* constructFromPrePost(int *pre, int length, int *post, int _) {
    a = pre;
    b = post;
    len = length;
    m = (char*)malloc(len + 1); // map v -> j
    for (int j = 0; j < len; ++j) m[b[j]] = j;
    i = 0; // preorder index
    const struct TreeNode *n = dfs();
    free(m);
    return n;
};