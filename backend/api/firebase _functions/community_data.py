from initialize_firebase import db
class CommunityDetails:

    def __init__(self, uid):
        # collection
        collection_ref = db.collection('community')
        docs = collection_ref.get()

        for doc in docs:
            if uid == doc.id:
                ID = uid
                Data = doc.to_dict()
                break

        def _id():
            return ID

        def _name():
            name = Data['Name']
            return name

        def _categories():
            categories = Data['categories']
            return categories

        def _description():
            description = Data['Description']
            return description

        self.id = _id()
        self.name = _name()
        self.categories = _categories()
        self.description = _description()


class CommunityChannel:
    def __init__(self, uid, channel):
        doc_roles_ref = db.document(f'community/{uid}/channels/{channel}/chat/roles')
        roles_privelages = doc_roles_ref.get()

        # chat collection
        chats_ref = db.document(f'community/{uid}/channels/{channel}/chat/messages')

        # Retrieve all chats
        chats = chats_ref.get()

        # all the chat ids are stored here
        self.messages = (chats.to_dict())

        # Check for document
        if roles_privelages.exists:
            self.roles = roles_privelages.to_dict()
        else:
            print("Document not found")  # change this into an api response


def ListCommunityChannels(uid):
    document_ref = db.collection('community').document(uid).collection('channels')

    # Retrieve all the channel documents
    docs = document_ref.get()

    # the channel ids are stored here
    channels = []

    for doc in docs:
        channel_id = doc.id
        channels.append(channel_id)

    return channels


def ListUsers(uid):
    global Data
    collection_ref = db.collection('community').document(uid).collection('members')
    docs = collection_ref.get()
    for doc in docs:
        Data = doc.to_dict()
    return Data



def CommunityJson(uid):
    com = CommunityDetails(uid)
    return {
        'id': com.id,
        'name': com.name,
        'categories': com.categories,
        'description': com.description
    }


'''# returns the community details as a json
print('---community details---')
com = CommunityJson('com1')
print(com)
# x-------------------------------x

# return the channel user roles and chat
channel = CommunityChannel('com1', 'channel-1')
print('---chat data---')
print(channel.messages)
# x-------------------------------x

# list all the channels in community
print('---list channels---')
channels = ListCommunityChannels('com1')
print(channels)
# x-------------------------------x
# list all the admin in community
print('---list roles---')
userlist = ListUsers('com1')
print(userlist)
# x-------------------------------x
'''
