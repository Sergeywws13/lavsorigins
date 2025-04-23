from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.types import FSInputFile

callback_router = Router()


# Словарь с путями к изображениям для каждого раздела
IMAGES = {
    "start": "images/1.png",
    "description": "images/description.jpg",
    "effect": "images/effect.jpg",
    "use": "images/use.jpg",
    "question": "images/1.png",
    "garant": "images/1.png",
    "expert_recommendations": "images/recommendation.png",
    "skin_type": "images/recommendation.png",
    "care_rules": "images/recommendation.png",
    "care_stages": "images/recommendation.png",
    "description_table": "images/foto_4.png",
    "foto_8": "images/foto_8.jpg",
    "foto_9": "images/foto_9.jpg",
}


async def edit_message_with_image(query: types.CallbackQuery, text: str, image_path: str, keyboard: InlineKeyboardMarkup):
    media = InputMediaPhoto(
        media=FSInputFile(image_path),
        caption=text
    )
    await query.message.edit_media(media=media, reply_markup=keyboard)


@callback_router.callback_query(lambda query: query.data == "description")
async def description_callback(query: types.CallbackQuery):
    await query.answer()
    
    text_part1 = """
Микротоковый массажёр для лица LAVSORIGINS модель NV-AP01 обладает следующими техническими характеристиками:
- Потребляемая мощность: 2.6 Вт ⚡
- Входное напряжение: 5 В постоянного тока
- Диапазон температур: 43-45°C 🌡️
- Частота вибрации: 7500-12000 об/мин 🌀
- Рабочее время: около 60 минут ⏰
- Время зарядки: около 90 минут 
- Емкость аккумулятора: 650 мАч 🔋
- Частота переменного тока: 20-40 кГц 📶
- Вес прибора: 87 г ⚖️
- Вес подставки: 19 г
- Время работы: 5 минут/таймер ⏰
    """
    
    keyboard_part1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ Преимущества", callback_data="desc_advantages")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="start")]
    ])
    
    await edit_message_with_image(
        query=query,
        text=text_part1,
        image_path=IMAGES["description"],
        keyboard=keyboard_part1
    )


@callback_router.callback_query(lambda query: query.data == "desc_advantages")
async def show_advantages(query: types.CallbackQuery):
    await query.answer()
    
    text_part2 = """
Преимущества:
✅ Красота и здоровье кожи лица, шеи и зоны декольте без уколов и оперативного вмешательства.
✅ Массажная головка прибора имеет каплевидную форму, что позволяет прорабатывать труднодоступные зоны лица вокруг глаз, а также стимулировать мышцы носогубной части лица.
✅ Наклон массажной головки 45° относительно прибора. Такая конструкция облегчает нагрузку на руку во время процедур.
✅ Удобен в использовании и подходит для домашнего применения.
✅ Компактный и легкий, что делает его идеальным для путешествий.
    """

    keyboard_part2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад к характеристикам", callback_data="description")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="start")]
    ])
    
    await edit_message_with_image(
        query=query,
        text=text_part2,
        image_path=IMAGES["description_table"],
        keyboard=keyboard_part2
    )


@callback_router.callback_query(lambda query: query.data == "effect")
async def effect_callback(query: types.CallbackQuery):
    await query.answer()

    text = """
🌟 Регулярное применение аппарата для лица LAVSORIGINS обеспечивает следующие эффекты: 🌟

🌿 Улучшение кровообращения и питания кожи:
- Улучшает кровообращение и лимфодренаж.
- Стимулирует обмен веществ в коже.

💧 Омоложение и восстановление:
- Увеличивает эластичность кожи, делает ее гладкой и увлажненной.
- Выравнивает тон кожи.
- Разглаживает мелкие морщинки на поверхности кожи.
- Способствует быстрому восстановлению кожи после лазерных процедур и пилинга.

🛑 Уменьшение отеков и воспалений:
- Уменьшает отечность.
- Помогает в лечении акне и розацеа.

💪 Укрепление мышц и контура лица:
- Укрепляет мышцы лица, улучшает их тонус и контур.

🔬 Биологические эффекты:
 - Стимулирует производство коллагена.
- Запускает клеточный метаболизм и активизирует процесс гидролиза жиров.
- Замедляет процессы преждевременного старения клеток кожи.
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")]
        ]
    )
    await edit_message_with_image(query, text, IMAGES["effect"], keyboard)


@callback_router.callback_query(lambda query: query.data == "use")
async def use_callback(query: types.CallbackQuery):
    await query.answer()

    text = """
✨ Способ применения микротокового массажёра LAVSORIGINS:

1. Очистите кожу, нанесите крем, сыворотку, гель или другую подходящую уходовую косметику.
2. Согласно таблице ниже выберите длительность и периодичность процедур.
3. Включите аппарат и выберите нужный режим.
4. Водите массажную головку по массажным линиям от центра к периферии.
5. Салфеткой удалите излишки косметического средства.
    """

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ См. таблицу режимов работы", callback_data="photo_8")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="start")]
    ])

    await edit_message_with_image(query, text, IMAGES["use"], keyboard)


@callback_router.callback_query(lambda query: query.data == "photo_8")
async def show_photo_8(query: types.CallbackQuery):
    await query.answer()

    text = "Таблица Использование косметических средств на разных режимах работы микротокового аппарата"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ См. таблицу процедур", callback_data="photo_9")],
        [InlineKeyboardButton(text="⬅️ Назад к инструкции", callback_data="use")]
    ])

    await edit_message_with_image(query, text, IMAGES["foto_8"], keyboard)


@callback_router.callback_query(lambda query: query.data == "photo_9")
async def show_photo_9(query: types.CallbackQuery):
    await query.answer()

    text = "Таблица Длительность и переодичность процедур"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад к таблице режимов работы", callback_data="photo_8")],
        [InlineKeyboardButton(text="⬅️ Назад к инструкции", callback_data="use")]
    ])

    await edit_message_with_image(query, text, IMAGES["foto_9"], keyboard)


@callback_router.callback_query(lambda query: query.data == "question")
async def question_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Задайте ваш вопрос о нашем продукте, и мы постараемся ответить вам в ближайшее время.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")]
        ]
    )
    await edit_message_with_image(query, text, IMAGES["question"], keyboard)


@callback_router.callback_query(lambda query: query.data == "garant")
async def garant_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
Гарантийные обязательства и брак продукции

Понятие «брак» означает дефект или недостаток устройства, возникшие при его производстве или транспортировке.

Заменить прибор можно в следующих случаях:
1. Прибор не включается (проверьте уровень заряда).
2. Прибор не заряжается от сети (обязательно проверьте зарядное устройство и USB-кабель, так как неисправность может быть в них).
3. Прибор не включается при полностью заряженном аккумуляторе.
4. Не работают кнопки прибора.
5. ЖК-экран массажера не отображает информацию об уровне заряда, режиме и уровне интенсивности при включенном приборе.
6. Присутствуют дефекты прибора (сколы, трещины, царапины на корпусе, массажной головке или контактной поверхности массажера).
7. Не работают электрические импульсы, вибрация или нагрев массажера (проверьте уровень регулировки интенсивности).

Гарантийный срок составляет 12 месяцев с даты продажи. Это основной срок.

Расширенная гарантия от продавца составляет 3 месяца к основной гарантии при соблюдении условий ее активации.

Если у вас возник гарантийный случай, следуйте инструкции:
1. Зайдите на сайт Wildberries в профиль покупателя.
2. Выберите «Возврат товара по браку».
3. Выберите товар из выпадающего списка или введите артикул товара.
4. Укажите причину возврата.
5. Добавьте фото и видео (если вы соблюдали условия активации расширенной гарантии, добавьте скриншот гарантийного талона с датой покупки из личного кабинета, нажав на кнопку «Срок годности»).
6. Оставьте комментарий (опишите проблему).
7. Отправьте заявку.

После этого мы проверим вашу заявку и примем решение. В ней появятся подробности о возврате, а статус заявки изменится.
"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")]
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)


@callback_router.callback_query(lambda query: query.data == "expert_recommendations")
async def expert_recommendations_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
Меня зовут Татьяна Горбатенко, я косметик-эстетист🌸
- Немного о себе: у меня высшее медицинское образование, в 2019 году я получила дополнительное образование по профессии Косметик - эстетист, уже более 4 лет забочусь о красоте и здоровье Вашей кожи. Чистки лица, пилинги, аппаратная косметология, мезотерапия, биоревитализация, массаж лица, уходовые процедуры, помогаю подобирать домашний уход по типу кожи.
Я протестировала на себе косметологический аппарат для лица LAVSORIGINS модель NV-AP01. Хочу отметить, что этот микротоковый массажер справляется с поставленными задачами, эффект от применения заметен. Советую добавить применение данного девайса в регулярный уход за кожей, чтобы стимулировать обновление клеток, улучшить тонус и упругость кожи, а также сократить видимость морщин.
Я также хочу рассказать Вам про типы кожи и правильный домашний уход. Эта тема раскроет правила красивой, сияющей и здоровой кожи лица. 

    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🧖 Типы кожи", callback_data="skin_type")],
            [InlineKeyboardButton(text="✨ Основные правила ухода", callback_data="care_rules")],
            [InlineKeyboardButton(text="⏰ Этапы домашнего ухода", callback_data="care_stages")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")]
        ]
    )
    await edit_message_with_image(query, text, IMAGES["expert_recommendations"], keyboard)


@callback_router.callback_query(lambda query: query.data == "skin_type")
async def skin_type_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
✅ РАЗЛИЧАЮТ 4 ТИПА КОЖИ:
- Сухая кожа тонкая и матовая. Ей не хватает увлажнения и естественной жировой смазки, которая защищает от агрессивного влияния внешней среды. При отсутствии должного ухода могут возникать покраснения, шелушения, ранние морщинки.
- Жирная кожа плотная, рельефная, с выраженными порами. Сальные железы работают очень активно, что провоцирует характерный блеск уже через несколько часов после умывания. Часто появляются черные точки, прыщи, угри, цвет лица выглядит тусклым.
- Комбинированная кожа — самый распространённый тип. При таком типе кожи чаще всего наблюдаются признаки жирной кожи в зоне лба, носа и подбородка. Периферия лица при этом склонна к сухости.
- Нормальная кожа — мечта всех женщин. Такая кожа выглядит увлажнённой, упругой, с естественным румянцем и сиянием. Нормальная кожа не требует особого ухода, но регулярная забота поможет ей оставаться сияющей и красивой.
Тип кожи мы получаем с рождения и он не меняется с возрастом. А вот состояние кожи может быть различным — под влиянием определенных факторов она становится проблемной, обезвоженной, чувствительной, появляются морщины и пигментные пятна. Тип кожи остаётся неизменным в течение всей жизни, тогда как состояние можно скорректировать специальным уходом.
Теперь Вы можете самостоятельно определить свой тип кожи.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="expert_recommendations")]
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)


@callback_router.callback_query(lambda query: query.data == "care_rules")
async def care_rules_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
✅ ОСНОВНЫЕ ПРАВИЛА УХОДА 
Итак, что же необходимо для правильного домашнего ухода, чтобы кожа радовала Вас каждый день. Все просто, главное следовать простым правилам.

💚 ПРАВИЛЬНО ПОДОБРАННАЯ УХОДОВАЯ КОСМЕТИКА
Очень важно подобрать уход по типу Вашей кожи, а также обращать внимание на состав косметики, она не должна содержать агрессивных компонентов, которые могут навредить. 

💚 РЕГУЛЯРНОСТЬ 
Очищение кожи лица обязательно утром и вечером, это должно стать Вашим маленьким ритуалом. Вечером вы удаляете остатки косметики и частицы пыли, а утром — излишки себума (кожного сала), который скопился за ночь.

💚 ПОСЛЕДОВАТЕЛЬНОСТЬ
Необходимо знать и помнить, что уходовые средства нужно наносить в правильной последовательности, тогда средства начнут работать правильно, что приведет к желаемому результату. 

💚 ПРАВИЛЬНАЯ ТЕХНИКА 
Косметику наносим легкими движениями по массажным линиям — от центра лица к периферии и от внешнего угла глаз к внутреннему.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="expert_recommendations")]
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)


@callback_router.callback_query(lambda query: query.data == "care_stages")
async def care_stages_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
Рассмотрим пункт ПОСЛЕДОВАТЕЛЬНОСТЬ подробнее, так как это одно из самых важных в домашнем уходе.
✅ ЭТАПЫ ДОМАШНЕГО УХОДА ЗА ЛИЦОМ
💚 Очищение
- Демакияж. Важный этап в очищении кожи. Для демакияжа используем мицеллярную воду или гидрофильное масло. Данные продукты поверхностно очищают от косметики и загрязнений. Утром этот шаг пропускаем. 
- Умывание. Мицеллярную воду и гидрофильное масло смываем гелем или пенкой для умывания. Данный этап пропускать нежелательно, так как на коже может оставаться тонкая плёнка после средств демакияжа, которая провоцирует раздражение, сухость и шелушение. Гель или пенка дополнительно очищают кожу от кожного сала и загрязнений. Помните, что кожу лица мыть до скрипа не нужно, это далеко не признак чистоты.
❗️ ВАЖНО ❗️ После умывания нельзя пользоваться полотенцем (т.к. при ежедневном использовании полотенца, в нем скапливаются нежелательные бактерии), лучше применять одноразовые бумажные салфетки или ватные диски. Лицо не трем.
💚 ТОНИЗИРОВАНИЕ
После умывания наносим тоник, он подготавливает кожу к дальнейшему уходу: восстанавливает рН, матирует, успокаивает и увлажняет.

💚 УВЛАЖНЕНИЕ 
Завершающий этап ежедневного ухода за кожей. Увлажнение необходимо любому типу кожи, даже если Ваша кожа жирная, она нуждается в данном этапе. Если нет достаточного увлажнения, то эластичность и упругость кожи снижается и появляются ранние морщины. Чтобы замедлить процесс старения и видеть здоровую, сияющую кожу лица, не забывайте наносить увлажняющие кремы по типу кожи. Также перед увлажнением можно наносить сыворотки. 
💚 ДОПОЛНИТЕЛЬНЫЙ УХОД
- Во время активного солнца утром за 30 минут до выхода на улицу наносим крема с защитой SPF 30, 50.
- Помимо ежедневного основного ухода 1–2 раза в неделю используйте средства для дополнительного ухода. Пилинги и энзимные пудры избавят от ороговевших клеток, придав лицу здоровое сияние, а маски напитают кожу полезными веществами.
Соблюдая такие простые правила, Ваша кожа скажет вам спасибо, а вы будете себя чувствовать уверенней.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="expert_recommendations")]
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)


@callback_router.callback_query(lambda query: query.data == "start")
async def start_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
🌟 Добрый день! 🌟

Используйте кнопки меню ниже. С удовольствием помогу вам!
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📜 Описание устройства", callback_data="description")],
            [InlineKeyboardButton(text="✨ Эффект", callback_data="effect")],
            [InlineKeyboardButton(text="🎯 Способ применения", callback_data="use")],
            [InlineKeyboardButton(text="💄 Рекомендации косметика-эстетиста", callback_data="expert_recommendations")],
            [InlineKeyboardButton(text="🤔 Задать вопрос?", callback_data="question")],
            [InlineKeyboardButton(text="📝 Гарантийные обязательства/Брак продукции", callback_data="garant")],
        ]
    )
    await edit_message_with_image(query, text, IMAGES["start"], keyboard)

