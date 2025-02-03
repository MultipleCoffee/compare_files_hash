import hashlib
 
def calculate_md5(file_path):
    """指定されたファイルのMD5ハッシュを計算"""
    try:
        with open(file_path, "rb") as f:
            md5_hash = hashlib.md5()
            while chunk := f.read(4096):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません: {file_path}")
        return None
    except PermissionError:
        print(f"❌ エラー: アクセス許可がありません: {file_path}")
        return None
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None
 
def main():
    # ユーザーに2つのファイルパスを入力させる
    file1 = input("比較する1つ目のファイルのパスを入力してください: ").strip()
    file2 = input("比較する2つ目のファイルのパスを入力してください: ").strip()
 
    # MD5ハッシュを計算
    hash1 = calculate_md5(file1)
    hash2 = calculate_md5(file2)
 
    # どちらかのハッシュが取得できなかった場合は終了
    if hash1 is None or hash2 is None:
        print("⚠️ ハッシュの計算に失敗しました。")
        return
 
    # ハッシュを表示
    print("\n--- ハッシュ値 ---")
    print(f"[{file1}] のMD5: {hash1}")
    print(f"[{file2}] のMD5: {hash2}")
 
    # 比較して結果を表示
    if hash1 == hash2:
        print("\n✅ ファイルは同じです！")
    else:
        print("\n❌ ファイルは異なります。")
 
if __name__ == "__main__":
    main()
