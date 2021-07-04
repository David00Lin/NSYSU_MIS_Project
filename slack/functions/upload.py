from slacker import Slacker
 
def main():
    # APIトークンを指定
    token = 'xoxb-2214572086944-2203570379105-qRC5h8VDVBAXIH90udvWpqfd'
    # アップロードするチャンネルを指定
    channel = 'C025E3Y3P70,U025ZGSB533'
    # 絶対パスを指定
    file = '/home/pi/Desktop/home work/Final_Project/slack/test01.jpg'
 
    slacker = Slacker(token)
    slacker.files.upload(file_=file, channels=channel)
 
if __name__ == "__main__":
    main()