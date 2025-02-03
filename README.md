# Compare Files Hash

## Overview
This repository provides two Python scripts for comparing file hashes:

1. `compare_file_hash.py`: Compares two specific files by calculating their hashes.
2. `compare_files_hash_in_directory.py`: Scans two specified directories and compares files with the same name by hashing them.

Both scripts use **SHA256** for hash comparison.

---

## Usage

### 1. Compare Two Specific Files
Run `compare_file_hash.py` to compare two files:
```sh
python compare_file_hash.py
```
Enter the file paths when prompted. The script will compute and compare their hashes.

### 2. Compare Files in Two Directories
Run `compare_files_hash_in_directory.py` to scan two directories and compare files with matching names:
```sh
python compare_files_hash_in_directory.py
```
Enter the paths of two directories when prompted. The script will list files with the same name and compare their hashes.

---

## Requirements
- Python 3.x
- No additional dependencies (uses built-in `hashlib` and `os` modules)

---

## 日本語説明

## 概要
このリポジトリには、ファイルのハッシュを比較する2つのPythonスクリプトが含まれています。

1. `compare_file_hash.py`：指定した2つのファイルのハッシュを計算して比較します。
2. `compare_files_hash_in_directory.py`：2つのディレクトリをスキャンし、同じファイル名のファイルを比較します。

どちらのスクリプトも**SHA256**を使用してハッシュを計算します。

---

## 使い方

### 1. 2つのファイルを比較
`compare_file_hash.py` を実行:
```sh
python compare_file_hash.py
```
プロンプトに従ってファイルのパスを入力すると、ハッシュを計算し比較します。

### 2. 2つのディレクトリ内のファイルを比較
`compare_files_hash_in_directory.py` を実行:
```sh
python compare_files_hash_in_directory.py
```
プロンプトに従ってディレクトリのパスを入力すると、同じファイル名のファイルをリストアップしてハッシュを比較します。

---

## 必要環境
- Python 3.x
- 追加のライブラリ不要（標準の `hashlib` と `os` を使用）
