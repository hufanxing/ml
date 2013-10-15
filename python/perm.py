
def all_perm(l, n, pre):
    if n == 0 :
        domains = {'com', 'net', 'cn', 'gov.cn', 'org', 'name', 'info', 'biz', 'cc', 'tv', 'me', 'co', 'so', 'tel', 'mobi', 'asia'}
        for domain in domains:
            print pre + '.' + domain
        return
    for i in l :
        all_perm(l, n-1, pre + i)


l='1234567890abcdefghizklmnopqrstuvwxyz'
# l='123'
for i in range(2, 4) :
    pre=''
    all_perm(l, i, pre)


