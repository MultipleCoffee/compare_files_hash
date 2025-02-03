import os
import hashlib
 
def calculate_hash(file_path, algorithm="SHA256"):
    """指定されたファイルのハッシュを計算（SHA256をデフォルト）"""
    try:
        hash_func = hashlib.new(algorithm.lower())
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません: {file_path}")
        return None
    except PermissionError:
        print(f"❌ エラー: アクセス許可がありません: {file_path}")
        return None
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None
 
def list_files_in_directory(directory):
    """指定ディレクトリ直下のファイルをリスト化"""
    try:
        return {file: os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))}
    except Exception as e:
        print(f"❌ エラー: {e}")
        return {}
 
def compare_directories(dir1, dir2):
    """2つのディレクトリ直下のファイルを比較"""
    files1 = list_files_in_directory(dir1)
    files2 = list_files_in_directory(dir2)
 
    # 共通のファイル名を抽出
    common_files = set(files1.keys()).intersection(set(files2.keys()))
 
    if not common_files:
        print("✅ 同じ名前のファイルは見つかりませんでした。")
        return
 
    for filename in common_files:
        path1 = files1[filename]
        path2 = files2[filename]
 
        print(f"\n=== ファイル名: {filename} の比較 ===")
        print(f"- {path1}")
        print(f"- {path2}")
 
        # ハッシュを計算して比較
        hash1 = calculate_hash(path1)
        hash2 = calculate_hash(path2)
 
        if hash1 is None or hash2 is None:
            print("⚠️ ハッシュの計算に失敗しました。")
            continue
 
        print("\n--- ハッシュ値 ---")
        print(f"[{path1}] のSHA256: {hash1}")
        print(f"[{path2}] のSHA256: {hash2}")
 
        if hash1 == hash2:
            print("✅ ファイルは同じです！")
        else:
            print("❌ ファイルは異なります。")
 
def main():
    # 2つのディレクトリパスを入力
    dir1 = input("1つ目のディレクトリのパスを入力してください: ").strip()
    dir2 = input("2つ目のディレクトリのパスを入力してください: ").strip()
 
    # ディレクトリの存在確認
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        print("❌ エラー: いずれかのディレクトリが存在しません。")
        return
 
    # ディレクトリを比較
    compare_directories(dir1, dir2)
 
if __name__ == "__main__":
    main()
