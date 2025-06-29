# Syntax 1
# file = open('youtube.txt', 'w')

# try:
#     file.write('Milan')
# finally:
#     file.close()

# Syntax 2
# with open('youtube.txt', 'w') as file:
#     file.write("Hello")



import json

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            test = json.load(file)                # json.load to  take datat from file and convert it to json
            # print(type(test))
            # print(test)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)       # it use to write in file it will take two parameter "what to write","where to write"

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 70)
    

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter new time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index seleted!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index seleted!")

def main():
    videos = load_data()

    while True:
        print("\n Youtubr Manager | choose an option")
        print("\n 1. List all youtube video ")
        print("\n 2. Add a youtube video ")
        print("\n 3. Update a youtube video detail ")
        print("\n 4. Delete a youtube video ")
        print("\n 5. Exit the app ")

        choice = input("Enter your choice: ")              # input will in string formate so note that either conver it into number or use it as string in future
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
                print("Invalid choice!")
                

if __name__ == "__main__":
    main()