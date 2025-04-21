from aiogram import Router, types

callback_router = Router()

@callback_router.callback_query(lambda query: query.data == "description")
async def description_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Микротоковый массажёр для лица LAVSORIGINS модель NV-AP01 обладает следующими техническими характеристиками:
    - Потребляемая мощность: 2.6 Вт
    - Входное напряжение: 5 В постоянного тока
    - Диапазон температур: 43-45°C
    - Частота вибрации: 7500-12000 об/мин
    - Рабочее время: около 60 минут
    - Время зарядки: около 90 минут
    - Емкость аккумулятора: 650 мАч
    - Частота переменного тока: 20-40 кГц
    - Вес прибора: 87 г
    - Вес подставки: 19 г
    - Время работы: 5 минут/таймер
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "effect")
async def effect_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Регулярное применение аппарата для лица LAVSORIGINS обеспечивает ощутимый эффект омоложения:
    - Улучшает кровообращение, лимфодренаж и обмен веществ в коже.
    - Улучшает эластичность кожи, делает ее гладкой и увлажненной.
    - Выравнивает тон кожи.
    - Уменьшает отечность.
    - Стимулирует производство коллагена.
    - Помогает в лечении акне, розацеа.
    - Укрепляет мышцы лица, улучшает их тонус и контур.
    - Разглаживает мелкие морщинки на поверхности кожи.
    - Способствует быстрому восстановлению кожи после лазерных процедур и пилинга.
    - Запускает клеточный метаболизм и активизирует процесс гидролиза жиров.
    - Замедляет процессы преждевременного старения клеток кожи.
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "use")
async def use_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Способ применения микротокового массажёра LAVSORIGINS:
    1. Очистите кожу, нанесите крем, сыворотку, гель или другую подходящую уходовую косметику.
    2. Согласно таблице ниже выберите длительность и периодичность процедур.
    3. Включите аппарат и выберите нужный режим.
    4. Водите массажную головку по массажным линиям от центра к периферии.
    5. Салфеткой удалите излишки косметического средства.
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "question")
async def question_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Задайте ваш вопрос о нашем продукте, и мы постараемся ответить вам в ближайшее время.
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "garant")
async def garant_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Гарантийный срок составляет 12 месяцев с даты продажи. Это основной срок.
    Расширенная гарантия от продавца составляет 3 месяца к основной гарантии, при соблюдении условий ее активации.
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "expert_recommendations")
async def expert_recommendations_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    Меня зовут Татьяна Горбатенко, я косметик-эстетист🌸
    - Немного о себе: у меня высшее медицинское образование, в 2019 году я получила дополнительное образование по профессии Косметик - эстетист, уже более 4 лет забочусь о красоте и здоровье Вашей кожи.
    """
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Типы кожи", callback_data="skin_type")],
            [types.InlineKeyboardButton(text="Основные правила ухода", callback_data="care_rules")],
            [types.InlineKeyboardButton(text="Этапы домашнего ухода", callback_data="care_stages")],
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)

@callback_router.callback_query(lambda query: query.data == "skin_type")
async def skin_type_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    РАЗЛИЧАЮТ 4 ТИПА КОЖИ:
    - Сухая кожа
    - Жирная кожа
    - Комбинированная кожа
    - Нормальная кожа
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "care_rules")
async def care_rules_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    ОСНОВНЫЕ ПРАВИЛА УХОДА
    - Правильная очистка кожи
    - Регулярность
    - Последовательность
    - Правильная техника
    """
    await query.message.answer(text)

@callback_router.callback_query(lambda query: query.data == "care_stages")
async def care_stages_callback(query: types.CallbackQuery):
    await query.answer()
    text = """
    ЭТАПЫ ДОМАШНЕГО УХОДА ЗА ЛИЦОМ
    - Очищение
    - Тонирование
    - Увлажнение
    - Дополнительный уход
    """
    await query.message.answer(text)
    