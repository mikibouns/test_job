from django.core.management.base import BaseCommand
from catalog_app.models import Category, HotelRoom, HotelCard, ReservedDates
from django.contrib.auth.models import User
from subprocess import call
import os
from random import randint
import datetime


try:
    os.remove('db.sqlite3')
    os.remove(r'D:\IGOR\PYTHON\test_job\test_project\catalog_app\migrations\0001_initial.py')
except:
    print('Not found!')

call('manage.py makemigrations', shell=True)
call('manage.py migrate', shell=True)

CATEGORY = [
    {'category_name': 'Junior Suite'},
    {'category_name': 'Suite'},
    {'category_name': 'De Luxe'},
    {'category_name': 'Duplex'},
    {'category_name': 'Family Room'},
    {'category_name': 'Studio'},
    {'category_name': 'Standart'},
    {'category_name': 'Village'},
    {'category_name': 'Apartament'},
    {'category_name': 'Honeymoon Room'}
]

HC = [
    {'hc_name': 'The Oberoi Udaivilas',
     'hc_description': 'Комплекс Oberoi находится в городе Удайпур на территории бывших охотничьих угодий потомков махараджей. Потрясающие виды на зелёный сад и озеро Пичола открываются отовсюду. Сам отель похож на замок, пребывание в котором посетители сравнивают с индийской сказкой.',
     'hc_title_img': r'\hotels\1.jpg'},
    {'hc_name': 'Baros Maldives',
     'hc_description': 'Этот титул отель получает уже в пятый раз. Главное отличие Baros Maldives в том, что он только для взрослых. Детей младше 8 лет здесь не принимают, ведь это место создано для отдыха в тишине.',
     'hc_title_img': r'\hotels\2.jpg'},
    {'hc_name': 'Armani Hotel Dubai',
     'hc_description': 'Неповторимый дизайн отеля разработал знаменитый модельер Джорджио Армани. Номера занимают 11 этажей небоскрёба в самом сердце Дубая. В знаменитый торговый центр Dubai Mall можно попасть прямо из лифта отеля. Из окон открывается панорамный вид на город и поющие фонтаны.',
     'hc_title_img': r'\hotels\3.jpg'},
    {'hc_name': 'Mriya Resort & Spa',
     'hc_description': 'У отеля есть собственный пляж, дорога до которого занимает всего 5 минут. К услугам гостей Mriya Resort & Spa 9 баров и ресторанов и ночной клуб. Любителям водных процедур придутся по вкусу крытый и открытый бассейны, спа-центр, сауна, хаммам и джакузи. Здесь можно заняться теннисом, сквошем или поиграть в боулинг. В отеле действует бесплатный кинотеатр.',
     'hc_title_img': r'\hotels\4.jpg'},
    {'hc_name': 'Dukes London',
     'hc_description': 'Отреставрированный исторический отель Dukes расположен в районе Мейфейр в Вестминстере. Самые интересные музеи, дворцы и брендовые магазины находятся совсем близко. Отель Dukes — это английская классика, дополненная современными удобствами. А вот мраморная баня здесь выполнена в итальянском стиле.',
     'hc_title_img': r'\hotels\5.jpg'},
    {'hc_name': 'Peninsula',
     'hc_description': 'Отель находится в Париже, совсем рядом с Триумфальной аркой. В первую очередь Peninsula — это роскошь и элегантность. Номера и холлы просторные, с высокими потолками и непременно украшены произведениями искусства. Многие считают Peninsula лучшим европейским отелем.',
     'hc_title_img': r'\hotels\6.jpg'},
    {'hc_name': 'Finch Bay Galapagos Hotel',
     'hc_description': 'Это уютный небольшой отель, который подойдёт любителям экзотической флоры и фауны. Здесь нет шумного веселья по вечерам, но это компенсируется живописными видами и обилием экскурсий. В некоторых номерах есть балконы с гамаками. Finch Bay Galapagos Hotel — прекрасное место для отдыха в тишине.',
     'hc_title_img': r'\hotels\7.jpg'},
    {'hc_name': 'The Venetian Macao Resort Hotel',
     'hc_description': 'The Venetian Macao — 39-этажный небоскрёб, седьмое по величине здание в мире, построенное в центре города. Вряд ли это хороший вариант для отдыха с детьми, зато взрослые здесь развлекаются от души. Это не только отель, но и огромное казино, развлекательная арена на 15 000 человек, множество выставочных и конференц-залов.',
     'hc_title_img': r'\hotels\8.jpg'},
    {'hc_name': 'San Clemente Palace Kempinski Venice',
     'hc_description': 'Kempinski — известнейшая сеть пятизвёздочных отелей, которой вот уже более ста лет. Отель San Clemente Palace находится в Венеции на собственном острове. На этом месте раньше был расположен монастырь, от которого осталась часовня XII века. По договорённости в ней проводят обряды венчания. Большую часть острова занимает парк, в котором посетители отеля могут загорать, бегать по дорожкам или пить коктейли у прудов.',
     'hc_title_img': r'\hotels\9.jpg'},
    {'hc_name': "Angel’s Marmaris",
     'hc_description': "Отель Angel’s Marmaris — это релаксация и забота о здоровье. К услугам гостей есть турецкая и паровая бани, сауна, джакузи и чудодейственная солевая комната. Особенностью отеля, помимо отсутствия алкоголя, является наличие отдельных бассейнов и пляжей только для женщин или мужчин. В таких условиях каждый почувствует себя комфортно.",
     'hc_title_img': r'\hotels\10.jpg'}
]

HR = [
    {'hr_category': 'Family Room',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\1_1.jpg',
     'hr_hotel': 'The Oberoi Udaivilas'},
    {'hr_category': 'Suite',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\1_2.jpg',
     'hr_hotel': 'The Oberoi Udaivilas'},
    {'hr_category': 'Village',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\1_3.jpg',
     'hr_hotel': 'The Oberoi Udaivilas'},
    {'hr_category': 'Suite',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\2_1.jpg',
     'hr_hotel': 'Baros Maldives'},
    {'hr_category': 'Village',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\2_2.jpg',
     'hr_hotel': 'Baros Maldives'},
    {
     'hr_category': 'Family Room',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\3_1.jpg',
     'hr_hotel': 'Armani Hotel Dubai'},
    {
     'hr_category': 'Suite',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\3_2.jpg',
     'hr_hotel': 'Armani Hotel Dubai'},
    {
     'hr_category': 'Suite',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\3_3.jpg',
     'hr_hotel': 'Armani Hotel Dubai'},
    {
     'hr_category': 'Family Room',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\3_4.jpg',
     'hr_hotel': 'Armani Hotel Dubai'},
    {
     'hr_category': 'Suite',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\4_1.jpg',
     'hr_hotel': 'Dukes London'},
    {
     'hr_category': 'Village',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\4_2.jpg',
     'hr_hotel': 'Dukes London'},
    {
     'hr_category': 'Village',
     'hr_description': 'description',
     'hr_title_img': r'\rooms\4_3.jpg',
     'hr_hotel': 'Dukes London'},
]


def users_iterator():
    for i in range(6):
        user = User(
            first_name='User{}'.format(i),
            email = 'user{}@mail.com'.format(i),
            username='User{}'.format(i),
        )
        user.set_password('123')
        yield user


class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.bulk_create(iter(users_iterator()))

        Category.objects.all().delete()
        for category in CATEGORY:
            new_category = Category(**category)
            new_category.save()

        HotelCard.objects.all().delete()
        for hotel_card in HC:
            new_hc = HotelCard(**hotel_card)
            new_hc.save()

        HotelRoom.objects.all().delete()
        for hr in HR:
            hr_hotel = hr['hr_hotel']
            hr_category = hr['hr_category']
            hr_category = Category.objects.get(category_name=hr_category)
            hr_hotel = HotelCard.objects.get(hc_name=hr_hotel)
            hr['hr_hotel'] = hr_hotel
            hr['hr_category'] = hr_category
            hr['hr_places'] = randint(1, 5)
            hr['hr_price'] = randint(10000, 100000)
            new_hr = HotelRoom(**hr)
            new_hr.save()

        ReservedDates.objects.all().delete()
        for i in range(20):
            start_date = datetime.date(randint(2019, 2019), randint(1, 2), randint(1, 28))
            last_date = start_date + datetime.timedelta(randint(1, 30))
            _id = randint(1, 12)
            new_rd = ReservedDates(
                check_in=start_date,
                check_out=last_date,
                room=HotelRoom.objects.get(id=_id),
                # person_id=1
            )

            new_rd.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser('admin', 'admin@mail.com', '123')
