text_main_menu = """
┏━━━━━━━━━━━ *Сустрэча* ━━━━━━━━━━━┓

    ━━ Знакомься 👱🏿‍♂️

    ━━ Приглашай друзей 💎

    ━━ Оформи анкету 🎨

┗━━━━━━ *Выбирай кнопку ниже* ━━━━━━┛
"""


text_main_menu_get_back = [
    "Рад снова тебя видеть! 😈",
    "Зачем ты удалил наш чат!? Ну ладно, заходи, я соскучился 🥹",
    "Какие люди в Голливуде! Проходи!",
    "Залетай ✈️",
]

text_search_profiles = "Смотреть анкеты 🔎"
text_edit_profile = "Редактировать свою анкету 🪞"
text_show_invite_code = "Инвайт-код для друга 💎"
text_go_to_deepseek = "Мне никто не пишет. . ."


def get_invite_message(available_invites: int, invite_code: str) -> str:
    message = f"""
Количество доступных приглашений: *{available_invites}*

Пригласительный код: *{invite_code}*
(после каждой активации этот код меняется)
"""
    return message