import vk_api
vk_session = vk_api.VkApi('79056363387', 'TU3IIU')
vk_session.auth()
vk = vk_session.get_api()

m_search = ['жизнь', 'знакомства', 'холостяк', 'прибыль', 'незнакомец', 'заработок']
report = open('report.txt', 'a+')

def addComment(post) :
    for id in post :
        print(id)
        report.write('https://vk.com/'+id.get(2))
        vk.wall.createComment(post_id=id, message='очень круто')
        

def postID(groups) :
    id_post = []
    for gr in groups :
        data = vk.wall.get(owner_id=-gr.get(0), count=10, offset=0)
        for key in data['items'] :
            id_post.append({0: key.get('owner_id'), 1: key.get('id'), 2: gr.get(1)})
    addComment(id_post)
                          
def searchGroupID(word) :
    spm_gr = []
    id_group = []
    search = vk.groups.search(q=word, count=10, offset=80)
    for key in search['items'] :
        if(key.get('is_closed') == 0) :
            d_post = vk.wall.get(owner_id=-key.get('id'), count=1, offset=0)
            if(d_post['items'][0].get('comments').get('count') > 0) :                
                id_group.append({0:key.get('id'), 1: key.get('screen_name')})
    postID(id_group)
            
    
for s in m_search :
    searchGroupID(s)
