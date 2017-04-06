from django.utils.safestring import mark_safe

class PageInfo:
    def __init__(self,current_page,all_count,per_item = 5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
    def start(self):
        return (self.CurrentPage)*self.PerItem

    def end(self):
        return self.CurrentPage *self.PerItem

    def all_pagr_count(self):
        temp = divmod(self.AllCount,self.PerItem)
        if temp[1] ==0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0]+1
        return all_page_count

def Pager(page,all_page_count):
    '''
    page: 当前页
    all_page_count:总页数
    '''
    page_html = []
    first_html = "<a href='index/%d'>首页</a>"%(1,)
    page_html.append(first_html)

    if page <= 1:
        prev_html = "<a href='#'>上一页</a>"
    else:
        prev_html = "<a href='/index/%d'>上一页</a>"%(page-1,)
    page_html.append(prev_html)

    if all_page_count < 12:
        begin = 0
        end = all_page_count
    else:
        if page<6:
            begin = 0
            end = 12
        else:
            if page+6>all_page_count:
                begin = page-6
                end = page + 5


    for i in range(all_page_count):
        if page == i+1:
            a_html = "<a class='selected' href='/index/%d'>%d</a>"%(i,)
        else:
            a_html = "<a href='/index/%d'>%d</a>"%(i+1,i+1)
        page_html.append(a_html)

    next_html = "<a href='/index/%d'>下一页</a>"%(page+1,)
    page_html.append(next_html)

    end_html = "<a href='/index/%d'>尾页</a>"%(all_page_count,)
    page_html.append(end_html)

    page_string= mark_safe(''.join(page_html))

    return page_string




