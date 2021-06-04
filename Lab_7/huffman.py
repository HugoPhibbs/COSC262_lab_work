"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False


class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
                self.left.__repr__(level + 1) + ',\n' +
                self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count))  # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """

    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label)  # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """

    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root

    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        output = ""
        for i in range(len(text)):
            chosen_letter = text[i]
            letter_binary = self.letter_traversal(chosen_letter, self.root)[:-1]
            output += letter_binary
        return output
            # find given binary code for this chosen letter.

    def letter_traversal(self, letter, node):
        # finds the binary expression for a given letter in a huffman tree using recursion
        if not node.is_leaf():
            left = '0' + self.letter_traversal(letter, node.left)
            right = '1' + self.letter_traversal(letter, node.right)
            if left.endswith('S'):
                return left
            else:
                return right
        else: # curr node is a leaf
            if node.char == letter:
                return "S"
            else:
                return "F"

    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        result = ""
        root = self.root
        for i in range(len(binary)):
            num = int(binary[i])
            if num == 1:
                next_node = root.right
                if next_node.is_leaf():
                    result += next_node.char
                    root = self.root
                else:
                    root = next_node
                # look at right subtree
            elif num == 0:
                next_node = root.left
                if next_node.is_leaf():
                    result += next_node.char
                    root = self.root
                else:
                    root = next_node
                # look at left subtree
        return result;

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        # Add all the letters from freqs into leaf objects and then into the tree array
        trees = []
        for (char, freq) in freqs.items():
            trees.append(Leaf(freq, char))
        # Run While loop to add the smallest two smallest count in the tree, until the tree has one node,
        # At that point the resultant tree is finished!
        while len(trees) > 1:
            # Sort trees again, so the botton two are always in order
            trees = sorted(trees, key=lambda x: x.count)
            # Need to handle when the freqs are the same, need to sort based on the lowest letter!
            (left, right) = self.get_left_right(trees)
            # Remove them both from the tree, and then add them back together in a node into the tree
            print(trees)
            trees.remove(left)
            trees.remove(right)
            print(trees)
            trees.append(Node(left, right))
        # Assign the root of the huffman tree to be the what is left in the trees list
        self.root = trees.pop()

    def get_left_right(self, trees):
        """gets the left and right nodes to choose, taking into account nodes that have the same frequency"""
        # for all nodes that have the same letter, sort these items too
        # go through the list, and for the first two frequencies, add all the nodes with these frequencies to the list
        # how to find the less most node in an array?

        # Get the freq of the first two trees in the trees array
        first_freq = trees[0].count
        second_freq = trees[1].count
        # Go through tree and add trees that have the same freq of first, may be only one tree
        first_same_freqs = self.get_left_right_helper(trees, first_freq)
        # Check if the second freq is different from first
        if first_freq != second_freq:
            # Is the same, so do the same process as with first freqs
            second_same_freqs = self.get_left_right_helper(trees, second_freq, 1)
            second_same_freqs = sorted(second_same_freqs, key=lambda x: self.find_smallest_node_letter(x).char)
        else:
            # Set second same freqs to equal empty list
            second_same_freqs = []
        # Sorrt first_same_freqs according to the lowest char in their trees
        first_same_freqs = sorted(first_same_freqs, key=lambda x:self.find_smallest_node_letter(x).char)
        # Combine the two sorted lists, works when second_same_freqs is zero.
        combined_freqs = first_same_freqs + second_same_freqs
        # Get left and right, left being the smallest node, right being the second smallest
        # There may have been the effect of smallest letter, works well anyways
        left = combined_freqs[0]
        right = combined_freqs[1]
        return (left, right)

    def get_left_right_helper(self, trees, freq, i=0, same_freqs=[]):
        """Helper method for above, creates a list of the same freq as freq"""
        # While the curr item in trees has the desired freq, continue iterating over it
        # adding it to the result as you go along
        while trees[i].count == freq:
            same_freqs.append(trees[i])
            i+=1
            if i == len(trees):# When we get down two items in our tree
                break
        return same_freqs

        ## go thru list and sort the nodes that sta
    def find_smallest_node_letter(self, node, min_letter_node=Leaf(-1, 'z')):
        """"Finds the smallest letter belonging to a treein a given tree"""
        if not node.is_leaf():
            left = node.left
            right = node.right
            return sorted([left, right], key=lambda x: self.find_smallest_node_letter(x).char)[0]
        else:
            if node.char < min_letter_node.char:
                min_letter_node = node
            return min_letter_node

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    tree = HuffmanTree()
    tree_string = """Node(42,
      Node(17,
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(25,
        Node(10,
          Node(5,
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c')))
    """
    tree.build_from_string(tree_string)
    print(tree)
    tree.plot()

    # Or you can build the tree directly
    tree2 = HuffmanTree(Node(
        Node(
            Leaf(8, 'b'),
            Leaf(9, 'a')),
        Node(
            Node(
                Node(
                    Leaf(2, 'f'),
                    Leaf(3, 'd')),
                Leaf(5, 'e')),
            Leaf(15, 'c'))))
    print(tree2)
    tree2.plot()


# The example from the notes
freqs = {'a': 9,
         'b': 8,
         'c': 15,
         'd': 3,
         'e': 5,
         'f': 2}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)