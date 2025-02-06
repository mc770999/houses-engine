import os
import sys


def print_tree(directory, prefix=''):
    # Get sorted list of items in the current directory
    items = sorted(os.listdir(directory))
    count = len(items)
    for index, item in enumerate(items):
        path = os.path.join(directory, item)
        # Choose the branch connector depending on position
        if index == count - 1:
            connector = '└── '
            new_prefix = prefix + '    '
        else:
            connector = '├── '
            new_prefix = prefix + '│   '
        print(prefix + connector + item)
        # If the item is a directory, recursively print its contents
        if os.path.isdir(path):
            print_tree(path, new_prefix)


if __name__ == '__main__':
    # print(sys.argv)
    # if len(sys.argv) != 2:
    #     print("Usage: python tree_script.py <directory>")
    #     sys.exit(1)
    root_dir = 'C:\\Users\\770mc\\PycharmProjects\\yad2all_engine\\app'
    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a directory or does not exist.")
        sys.exit(1)

    # Print the root directory name
    print(root_dir)
    print_tree(root_dir)