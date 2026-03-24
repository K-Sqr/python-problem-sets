"""
Test Suite for Unit 8 - Binary Trees
Topics: Tree construction, traversal, properties, recursive algorithms
"""
import pytest


class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestUnit8BinaryTrees:
    """Unit 8: Binary Trees - Construction and Properties"""
    
    def test_build_binary_tree(self):
        """Test: Build a binary tree with 3 nodes"""
        # Problem 1: Create a tree structure
        #   10
        #  /  \
        # 3    6
        
        root = TreeNode(10, TreeNode(3), TreeNode(6))
        
        assert root.val == 10
        assert root.left.val == 3
        assert root.right.val == 6
        assert root.left.left is None
        assert root.left.right is None
    
    def test_check_tree_basic(self):
        """Test: Check if root equals sum of children (3 nodes)"""
        # Problem 2: Root should equal sum of left + right children
        
        def check_tree(root):
            return root.val == (root.left.val + root.right.val)
        
        # True case: 10 = 4 + 6
        tree_true = TreeNode(10, TreeNode(4), TreeNode(6))
        assert check_tree(tree_true) is True
        
        # False case: 5 ≠ 3 + 1
        tree_false = TreeNode(5, TreeNode(3), TreeNode(1))
        assert check_tree(tree_false) is False
    
    def test_check_tree_with_optional_children(self):
        """Test: Check sum property with 1, 2, or 3 nodes"""
        # Problem 3: Handle trees with missing children
        
        def check_tree(root):
            if not root.left and not root.right:
                # No children
                return False
            elif not root.left:
                # Only right child
                return root.val == root.right.val
            elif not root.right:
                # Only left child
                return root.val == root.left.val
            else:
                # Both children
                return root.val == (root.left.val + root.right.val)
        
        # Two children: 10 = 10 + 0 (False) but let's test valid case
        tree_both = TreeNode(10, TreeNode(5), TreeNode(5))
        assert check_tree(tree_both) is True
        
        # Only right child: 10 = 10 ✓
        tree_right_only = TreeNode(10, None, TreeNode(10))
        assert check_tree(tree_right_only) is True
        
        # Only left child: 10 = 10 ✓
        tree_left_only = TreeNode(10, TreeNode(10), None)
        assert check_tree(tree_left_only) is True
        
        # No children
        tree_no_children = TreeNode(5, None, None)
        assert check_tree(tree_no_children) is False
    
    def test_leftmost_node(self):
        """Test: Find the leftmost (deepest left) node"""
        # Problem 4: Traverse to the leftmost leaf node
        
        def left_most(root):
            if root is None:
                return None
            
            curr = root
            while curr.left is not None:
                curr = curr.left
            
            return curr.val
        
        # Simple tree:
        #     1
        #    / \
        #   2   5
        #  / \
        # 4   3
        tree = TreeNode(1, 
                       TreeNode(2, TreeNode(4), TreeNode(3)),
                       TreeNode(5))
        assert left_most(tree) == 4
        
        # Single node
        single = TreeNode(42)
        assert left_most(single) == 42
        
        # Left-skewed tree
        #     10
        #    /
        #   9
        #  /
        # 8
        left_skew = TreeNode(10, TreeNode(9, TreeNode(8)))
        assert left_most(left_skew) == 8
    
    def test_leftmost_node_none(self):
        """Test: Handle None root"""
        def left_most(root):
            if root is None:
                return None
            
            curr = root
            while curr.left is not None:
                curr = curr.left
            
            return curr.val
        
        assert left_most(None) is None


class TestUnit8TreeTraversal:
    """Traversal patterns and tree properties"""
    
    def test_tree_height(self):
        """Test: Calculate height of binary tree"""
        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        #     1
        #    / \
        #   2   3
        #  /
        # 4
        tree = TreeNode(1,
                       TreeNode(2, TreeNode(4)),
                       TreeNode(3))
        assert height(tree) == 3
        
        assert height(TreeNode(1)) == 1
        assert height(None) == 0
    
    def test_count_nodes(self):
        """Test: Count total nodes in tree"""
        def count_nodes(root):
            if root is None:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)
        
        tree = TreeNode(1,
                       TreeNode(2, TreeNode(4)),
                       TreeNode(3))
        assert count_nodes(tree) == 4
        
        assert count_nodes(TreeNode(1)) == 1
        assert count_nodes(None) == 0
