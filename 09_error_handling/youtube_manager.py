import json

# //load data part
def load_data():
    try:
        with open('youtube.txt','r')as file:
            test =json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
        return []

#  save the data part   
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
           json.dump(videos,file)

# list all videos
def list_all_videos(videos):
    print("\n")
    print("*" *60)
    for index ,video in enumerate(videos,start=1):
       
        print(f"{index}. {video['name']},Duration:{video['time']} ")
    print("\n")
    print("*" *60)

# add the videos    
def add_video(videos):
    name=input("Enter the video name:")
    time=input("Enter the video time:")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

# Update the videos part    
def update_video(videos):
    pass


# delete video part
def delete_video(videos):
    pass

# // main execution is started here
def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager")
        print("1.List all youtube videos")
        print("2.Add a youtube video")
        print("3.update the youtube video")
        print("4.Delete the youtube videio")
        print("5.Exit the app")
        choice=input("enter your choice")
        # print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)  
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break        
            case _:
                print("Invalid choice")
                   
if __name__=="__main__":
    main()                   