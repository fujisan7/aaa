import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_videos(source_folder, output_folder, source_ext, target_ext):
    """
    指定したフォルダ内の動画ファイルを指定されたフォーマットに変換します。
    
    Args:
        source_folder (str): 変換元の動画ファイルがあるフォルダのパス
        output_folder (str): 変換後の動画ファイルを保存するフォルダのパス
        source_ext (str): 変換元の動画ファイルの拡張子
        target_ext (str): 変換先の動画ファイルの拡張子
    """
    # 出力フォルダがない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 変換対象のファイルを検索
    files = [f for f in os.listdir(source_folder) if f.endswith(source_ext)]
    
    # 進行状況バーでファイルを一つずつ処理
    for file in tqdm(files, desc="変換中"):
        full_path = os.path.join(source_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.' + target_ext)
        clip = VideoFileClip(full_path)
        clip.write_videofile(output_path, codec="libx264")
        clip.close()

def main():
    source_folder = input("変換元の動画があるフォルダのパスを入力してください: ")
    output_folder = input("変換後の動画を保存するフォルダのパスを入力してください: ")
    source_ext = input("変換元の動画ファイルの拡張子を入力してください (例: mp4): ")
    target_ext = input("変換先の動画ファイルの拡張子を入力してください (例: avi): ")
    
    convert_videos(source_folder, output_folder, source_ext, target_ext)

if __name__ == "__main__":
    main()
