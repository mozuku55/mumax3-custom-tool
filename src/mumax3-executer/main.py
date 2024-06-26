from execute import Execute
import sys
import os

def main():
    args = sys.argv
    print(args)
    if len(args) <  3:
        print("src/mumax3-executer/main.py : not enough args")
        return
    abs_path = os.path.abspath(args[2]) 
    if len(args) >= 3 and args[1] == 'dryrun':
        execute_in_bulk(abs_path, True)
    if len(args) >= 3 and args[1] == 'exec':
        execute_in_bulk(abs_path, False)
    return

def execute_in_bulk(dir_path:str, is_dryrun:bool = True):
    mx3_paths = find_mx3_files(dir_path)
    print(f"exec mx3 : {mx3_paths}")
    for mx3_path in mx3_paths:
        print(f"exec mx3 : {mx3_path}")
        if not is_dryrun:
            Execute(mx3_path, is_dryrun)
    return

def find_mx3_files(dir_path:str):
    mx3_paths = []
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        # mx3ファイルの存在確認
        is_mx3_file = os.path.isfile(item_path) and item.endswith(".mx3")
        # dir確認
        is_dir = os.path.isdir(item_path)
        is_out_dir = item.endswith(".out")
        # outディレクトリの存在確認
        name, _  = os.path.splitext(item_path)
        print(f"basename : {name}")
        outdir_path = os.path.join(os.path.dirname(item_path), f"{name}.out")
        print(f"outdir : {outdir_path}")
        is_outdir_exist = os.path.exists(outdir_path) and os.path.isdir(outdir_path)

        if is_mx3_file:
            if not is_outdir_exist:
                mx3_paths.append(item_path)
            else:
                print(".outがすでに存在します")
        elif is_dir and not is_out_dir:
            mx3_paths.extend(find_mx3_files(item_path))
    return mx3_paths

main() 



