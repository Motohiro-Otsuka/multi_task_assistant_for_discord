
"""
各画面で使用する共通的な設定など
"""

#screenの種類とフレームを定義する。
#フレームは画面切り替えと同時にdestroyされるので最初はNoneを入れておく
screens = {
    "select_base_config": None,
    "common":None,
    "parrot":None,
    "chat_openai":None,
    "live_scheduler":None,
}
#botのconfig dict型
config = None

def str_to_bool(text):
    if(text=="True"):
        return True
    else:
        return False

def wrapper_show_select_base(root):
    from select_base_config import select_base
    select_base(root)

def wrapper_edit_common_config(root):
    from edit_common_config import edit_common_config
    edit_common_config(root)

def wrapper_edit_parrot_config(root):
    from edit_parrot_config import edit_parrot_config
    edit_parrot_config(root)

def wrapper_edit_chat_config(root):
    from edit_chat_config import edit_chat_config
    edit_chat_config(root)

def wrapper_edit_live_scheduler_config(root):
    from edit_live_scheduler_config import edit_live_scheduler_config
    edit_live_scheduler_config(root)

def wrapper_edit_live_scheduler_img_config(root):
    from edit_live_scheduler_config import edit_live_scheduler_img_config
    edit_live_scheduler_img_config(root)

def wrapper_edit_live_scheduler_grid_config(root):
    from edit_live_scheduler_config import edit_live_scheduler_grid_config
    edit_live_scheduler_grid_config(root)

def wrapper_end_screen(root):
    from end_screen import end_screen
    end_screen(root)