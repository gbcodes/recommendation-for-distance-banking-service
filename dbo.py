import pandas as pd



def korpi(korp, sec, intbank,inb,isp,price_b,isp_b, bankclient, interf):
    # sec = input('Важна ли вам безопасность? ')



    str(sec).lower()
    str(intbank).lower()
    str(bankclient).lower()
    str(interf).lower()
    str(inb).lower()
    str(isp).lower()
    str(price_b).lower()
    str(isp_b).lower()

    if sec == 'да':
        bank = korp.loc[korp['Безопасность'] >= 7]
    else:
        bank = korp

    # intbank = input('Нужен ли вам интернет банкинг? ')

    if intbank == 'да':
        bank = bank.loc[bank['Интернет-банкинг(подключение)'] == 1]

        # inb = input('Важна ли вам низкая цена за подключение интернет банкинга? ')
        if inb == 'да':
            bank = bank.loc[bank['Цена'] <= 500]

        # isp = input('Важна ли вам низкая цена за обслуживание интернатом банкингом? ')
        if isp == 'да':
            bank = bank.loc[bank['Интернет-банкинг(использование)'] <= 1400]
    else:
        bank = bank.loc[bank['Интернет-банкинг(подключение)'] == 0]

    # bankclient = input('Нужен ли вам банк клиент? ')

    if bankclient == "да":
        bank = bank.loc[bank['Банк-клиент(подключение)'] == 1]
        # price_b = input('Важна ли вам низкая цена на подключение банка клиента? ')
        if price_b == 'да':
            bank = bank.loc[bank['Цена.1'] <= 1300]
        # isp_b = input('Важна ли вам низкая цена за обслуживание? ')
        if isp_b == 'да':
            bank = bank.loc[bank['Банк-клиент(использование)'] <= 600]
    else:
        bank = bank.loc[bank['Банк-клиент(подключение)'] == 0]

    # interf = input('Важно ли вам удобство интерфейса? ')

    if interf == 'да':
        bank = bank.loc[bank['Удобство интерфейса'] >= 6]

    # funct = input('Нужен ли вам широкий функционал? ')

    if bank.empty:
        res = korp.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)', ascending=False)
        return 'Мы вам рекомендуем: ' + '\n'.join(res['Название'][:3])
    else:
        result = bank.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)',
                                  ascending=False)
        return 'Мы вам рекомендуем: ' + ' ,'.join(result['Название'][:3])


def fizi(sec, sms, intbank, mob, vklad, credit, interf, price, inb, isp, pric, ispol, proc, pro):

    # sec1 = str(sec).lower().strip()
    # intbank1 = str(intbank).lower().strip()
    # sms1=str(sms).lower().strip()
    # mob1=str(mob).lower().strip()
    # credit1=str(credit).lower().strip()
    # interf1=str(interf).lower().strip()
    # inb1=str(inb).lower().strip()
    # isp1=str(isp).lower().strip()
    # price1=str(price).lower().strip()
    # ispol1=str(ispol).lower().strip()
    # vklad1=str(vklad).lower().strip()
    # pric1=str(pric).lower().strip()
    # proc1=str(proc).lower().strip()
    # pro1=str(pro).lower().strip()
    # sec = input('Важна ли вам безопасность? ')
    fiz=pd.read_excel('Fiz.xlsx')

    bank = fiz
    if sec == 'да':
        bank = bank[bank['Безопасность'] >= 5]


    # sms = input('Нужен ли вам смс банкинг? ')
    if sms == 'да':
        bank = bank[bank['SMS- банкинг'] == 1]
    #         price = input('Важна ли вам низкая цена за смс банкинг? ')
        if price == 'да':
            bank = bank[bank['Цена'] < 45 ]

    # intbank = input('Нужен ли вам интернет банкинг? ')

    if intbank == 'да':
        bank = bank[bank['Интернет-банкинг(подключение)'] == 1]

    #         inb = input('Важна ли вам низкая цена за подключение интернет банкинга? ')
    #     if inb == 'да':
    #         bank = bank[bank['Цена.1'] < 60]

        # isp = input('Важна ли вам низкая цена за обслуживание интернатом банкингом? ')
        if isp == 'да':
            bank = bank[bank['Интернет-банкинг(использование)'] < 500]
    else:
        bank = bank[bank['Интернет-банкинг(подключение)'] == 0]

    # mob = input('Нужен ли вам мобильный банк? ')
    if mob == 'да':
        bank = bank[bank['Мобильный банкинг(подключение)'] == 1]
    #         pric = input('Важна ли вам низкая плата за мобильный банк? ')
    #     if pric == 'да':
    #         bank = bank[bank['Цена.2'] < 60]
        # ispol = input('Важна ли вам низкая цена за использование?')
        if ispol == 'да':
            bank = bank[bank['Мобильный банкинг(использование)'] <= 30]


    # vklad = input('Нужна ли вам возможность открытия вклада?')
    if vklad == 'да':
        bank = bank[bank['Открытие вклада'] == 1]
    #         proc = input('Важен ли вам высокий процент по вкладу? ')
        if proc == 'да':
            bank = bank[bank['Процент по вкладу'] > 6]
    else:
        bank = bank[bank['Открытие вклада'] == 0]

    # credit = input('Нужна ли вам возможность брать кредит? ')
    if credit == 'да':
        bank = bank[bank['Оформление кредита'] == 1]
    #         pro = input('Важен ли вам низкий процент кредитования? ')
        if pro == 'да':
            bank = bank[bank['Процент по кредиту'] <= 11.9]


    # interf = input('Важно ли вам удобство интерфейса? ')

    # if interf == 'да':
    #     bank = bank[bank['Удобство интерфейса'] >= 6]

    # funct = input('Нужен ли вам широкий функционал? ')


    if bank.empty:
        res = fiz.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)', ascending=False)
        return 'Мы вам рекомендуем: ' + '\n'.join(res['Название'][:3])
    else:
        result = bank.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)', ascending=False)
        return 'Мы вам рекомендуем: ' + '\n'.join(result['Название'][:3])


def yuri(yur, sec, intbank, bankclient, mob, credit, interf, inb, isp, price_b, isp_b):



    if sec == 'да':
        bank = yur.loc[yur['Безопасность'] >= 5]
    else:
        bank = yur


    if intbank == 'да':
        bank = bank.loc[bank['Интернет-банкинг(подключение)'] == 1]

        # inb = input('Важна ли вам низкая цена за подключение интернет банкинга? ')
        if inb == 'да':
            bank = bank.loc[bank['Цена'] <= 600]

        # isp = input('Важна ли вам низкая цена за обслуживание интернатом банкингом? ')
        if isp == 'да':
            bank = bank.loc[bank['Интернет-банкинг(использование)'] <= 800]
    else:
        bank = bank.loc[bank['Интернет-банкинг(подключение)'] == 0]

    # bankclient = input('Нужен ли вам банк клиент? ')

    if bankclient == "да":
        bank = bank.loc[bank['Банк-клиент(подключение)'] == 1]
        # price_b = input('Важна ли вам низкая цена на подключение банка клиента? ')
        if price_b == 'да':
            bank = bank.loc[bank['Цена.1'] <= 800]
        # isp_b = input('Важна ли вам низкая цена за обслуживание? ')
        if isp_b == 'да':
            bank = bank.loc[bank['Банк-клиент(использование)'] <= 500]
    else:
        bank = bank.loc[bank['Банк-клиент(подключение)'] == 0]

    # mob = input('Нужен ли вам мобильный банк? ')
    if mob == 'да':
        bank = bank.loc[bank['Мобильный банк(подключение)'] == 1]
    else:
        bank = bank.loc[bank['Мобильный банк(подключение)'] == 0]

    # credit = input('Важна ли вам низкая ставка по кредиту? ')

    if credit == 'да':
        bank = bank.loc[bank['Минимальная ставка по кредиту'] <= 12]

    # interf = input('Важно ли вам удобство интерфейса? ')

    if interf == 'да':
        bank = bank.loc[bank['Удобство интерфейса'] >= 5]

    # funct = input('Нужен ли вам широкий функционал? ')

    if bank.empty:
        res = yur.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)', ascending=False)
        return 'Мы вам рекомендуем: ' + '\n'.join(res['Название'][:3])
    else:
        result = bank.sort_values(by='Уровень цен(чем меньше цены у банка, тем больше тут коэффициент)',
                                  ascending=False)
        return 'Мы вам рекомендуем: ' + ' ,'.join(result['Название'][:3])



def main():



    a = fizi('да','да','да','да','да','d','', '','','','','','','')
    print(a)



if __name__ == '__main__':
    main()
