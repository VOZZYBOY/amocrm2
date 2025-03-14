import os

def print_tree(path, level=0):
    if not os.path.exists(path):
        return
        
    items = sorted(os.listdir(path))
    
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            print("│   " * level + "├── " + f"[{item}]")
            print_tree(item_path, level + 1)
        else:
            print("│   " * level + "├── " + item)

if __name__ == "__main__":
    print_tree(".") 