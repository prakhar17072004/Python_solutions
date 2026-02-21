import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor = conn.curser()

cursor.execute(''' 
      CREATE TABLE IF NOT EXIST videos(
               id INTGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL 
               )
''')

def list_videos(videos):
    pass
    
def add_videos(videos):
    pass

def update_videos(videos):
    pass

def delete_videos(videos):
    pass



def main():
    while True:

        print("\nYoutube manger app with DB") 
        print("1.List Videos")
        print("2.Add Videos")
        print("3.Update Videos ")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice :")

        if choice =='1':
            list_videos()
        elif choice == '2':
            name=input("Enter the videos name :")
            time= input("Enter the video time")
            add_videos(name,time)
        elif choice == '3':
            videos_id=input("Enter the video id for update :")
            name=input("Enter the videos name :")
            time= input("Enter the video time")
            update_videos(videos_id,name,time)

        elif choice == '4':
            videos_id=input("Enter the video id for update :")
            
            delete_videos(videos_id) 
        elif choice == '5':
            break 
        else:
            print("Invalid choice ")      

    conn.close()

if __name__ == "__main__":
    main()