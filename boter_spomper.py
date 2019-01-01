import vk_api
vk_session = vk_api.VkApi('79056363387', 'TU3IIU')
vk_session.auth()
vk = vk_session.get_api()

m_search = ['жизнь', 'знакомства', 'холостяк', 'прибыль', 'незнакомец', 'заработок']

def addComment(post) :
    for id in post :
        print(id.get(1))
        """vk.wall.createComment(post_id=id, message='хочу пообщаться, мой телеграм всегда открыт для вас https://t.me/markmarushak')"""

def postID(groups) :
    id_post = []
    for gr in groups :
        data = vk.wall.get(owner_id=-gr, count=10, offset=0)
        for key in data['items'] :
            id_post.append({0: key.get('owner_id'), 1: key.get('id')})
    #bot.send_message(chat_id=update.message.chat_id, text=id_post)
    print(id_post)
                          
def searchGroupID(word) :
    spm_gr = []
    id_group = []
    search = vk.groups.search(q=word, count=1000, offset=30)
    for key in search['items'] :
        if(key.get('is_closed') == 0) :
            d_post = vk.wall.get(owner_id=-key.get('id'), count=1, offset=0)
            if(d_post['items'][0].get('comments').get('count') > 0) :
                #bot.send_message(chat_id=update.message.chat_id, text='https://vk.com/'+key.get('screen_name'))
                id_group.append(key.get('id'))
    postID(id_group)
            
    
for s in m_search :
    searchGroupID(s)
