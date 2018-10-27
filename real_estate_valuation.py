# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
import config  # Считать параметры из конфигурационного файла


def main():
    print(Fore.GREEN + '\n         Программа оценки окупаемости объекта недвижимости')
    print(Fore.GREEN + '====================================================================')
    print(Style.RESET_ALL)

    #################################################################################
    # Ввод площади объекта, кв.м.
    print 'Введите площадь объекта, кв.м.: ',
    building_area = input()
    # building_area = 31.5

    # Ввод стоимости права аренды, руб в год
    print 'Введите стоимость права аренды, руб/год: ',
    rent_rights_cost = input()
    # rent_rights_cost = 123952.5

    #################################################################################
    # Вывод постоянных пораметров из конфигурационного файла
    if config.CONFIG_PARAMETERS_PRINT:
        print '\n-------------------------------------------------'

        print "Средняя стоимость аренды в месяц: {0:.2f} руб".format(config.AVERAGE_RENTAL)
        print "Количество доходных месяцев в году: {0}".format(config.PROFIT_MONTHS)
        print "Стоимость предварительного ремонта за 1 кв.м.: {0:.2f} руб".format(config.REPAIR)

        print "Стоимость регистрации договора: {0:.2f} руб".format(config.CONTRACT_REGISTRATION)
        print "Мелкие расходы на запуск объекта: {0:.2f} руб".format(config.RUNNING_COST)

        print "Стоимость отопления в месяц за 1 кв.м.: {0:.2f} руб".format(config.HEATING)
        print "Обслуживание ЖЭКом в месяц: {0:.2f} руб".format(config.HOUSING_OFFICE)
        print "Минимальная страховка за 1 кв.м. в месяц: {0:.2f} руб".format(config.MIN_INSURANCE)
        print "Бухгалтерское обслуживание в месяц: {0:.2f} руб".format(config.ACCOUNTING_SERVICE)

        print "Требуемый коэффициент доходности: {0}".format(config.REQUIRED_PROFIT_MARGIN)

    #################################################################################
    # *** Расчёт неосновных параметров ***

    # Страховка всей площади в месяц, руб
    month_all_area_insurance = building_area * config.MIN_INSURANCE

    # Стоимость отопления в месяц, руб
    month_heating = config.HEATING * building_area

    # Обслуживание ЖЭКом в месяц, руб
    month_housing_office = config.HOUSING_OFFICE * building_area

    if config.OPTIONAL_CALCULATED_PARAMETERS_PRINT:
        print '\n-------------------------------------------------'
        print('Страховка в месяц всей площади: {0:.2f} руб/мес'.format(month_all_area_insurance))
        print('Отопление в месяц всей площади: {0:.2f} руб/мес'.format(month_heating))
        print('Обслуживание ЖЭКом в месяц всей площади: {0:.2f} руб/мес'.format(month_housing_office))

    #################################################################################
    # *** Расчёт основных параметров ***

    # Доход от аренды в месяц
    month_rental_income = building_area * config.AVERAGE_RENTAL

    # Выплаты за аренду в месяц
    month_rental_payout = rent_rights_cost / 12

    # Расходы в месяц
    month_payout = \
        month_rental_payout + \
        month_all_area_insurance + \
        month_heating + \
        month_housing_office + \
        config.ACCOUNTING_SERVICE + \
        (config.CONTRACT_REGISTRATION + config.RUNNING_COST) / config.RENT_TIME / 12

    # Доход в год с учётом несдаваемых месяцев
    year_rental_income = building_area * config.AVERAGE_RENTAL * config.PROFIT_MONTHS

    # Коэффициент доходности
    profit_margin = (year_rental_income - month_payout * 12) / (config.CONTRACT_REGISTRATION + config.RUNNING_COST)

    # Безубыточность сдачи, руб/кв.м. в месяц
    loss_free_rent = ((month_payout * 12) / 10) / building_area

    print '\n-------------------------------------------------'
    print('Доход от аренды в месяц: {0:.2f} руб'.format(month_rental_income))
    print('Выплаты за аренду в месяц: {0:.2f} руб'.format(month_rental_payout))
    print('Расходы в месяц: {0:.2f} руб'.format(month_payout))
    print
    print('Доход от аренды в год (за {0} месяцев): {1:.2f} руб'
          .format(config.PROFIT_MONTHS, year_rental_income))
    print('Расходы в год (за 12 месяцев): {0:.2f} руб'.format(month_payout * 12))

    if profit_margin >= config.REQUIRED_PROFIT_MARGIN:
        print('Коэффициент доходности (лучше требуемого "{0}"): '.format(config.REQUIRED_PROFIT_MARGIN) +
              Fore.GREEN + '{0:.0f}'.format(profit_margin))
    else:
        print('Коэффициент доходности (хуже требуемого "{0}"): '.format(config.REQUIRED_PROFIT_MARGIN) +
              Fore.RED + '{0:.0f}'.format(profit_margin))
    print(Style.RESET_ALL)
    print
    print('Минимальная стоимость аренды: {0:.2f} руб'.format(loss_free_rent))

    #################################################################################


if __name__ == '__main__':
    main()
