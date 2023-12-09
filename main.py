from instagrapi import Client
import pandas as pd

cl = Client()
cl.login('eatit.uk', 'jDWw2kQY')

# Instagram data retrieval
user_id = cl.user_id_from_username('eatit.uk')
medias = cl.hashtag_medias_top_a1('SmallBusinessUK', 100)

# Create a DataFrame to hold the Instagram data
data = {'Username': [], 'Full Name': [], 'Bio': []}

# Initialize a set to keep track of unique usernames
unique_usernames = set()

# Iterate through Instagram data
for media in medias:
    user_info = media.user
    user_details = cl.user_info(user_info.pk)

    user_name = user_info.username

    # Check if the username is not already in the set
    if user_name not in unique_usernames:
        unique_usernames.add(user_name)

        user_full_name = user_details.full_name
        user_bio = user_details.biography

        # Append data to the DataFrame
        data['Username'].append(user_name)
        data['Full Name'].append(user_full_name)
        data['Bio'].append(user_bio)
# Create or load the Excel file
excel_path = r"C:\Users\sasha\Desktop\Business Contacts.xlsx"

# Append the new data to the existing DataFrame
df = pd.DataFrame(data)

# Write the DataFrame back to the Excel file
df.to_excel(excel_path, index=False)

# Print a message indicating the completion
print("Data appended to Excel file.")