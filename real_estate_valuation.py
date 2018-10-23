# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
import config       # Считать параметры из конфигурационного файла


def main():
    print(Fore.GREEN + '\n         Программа оценки окупаемости объекта недвижимости')
    print(Fore.GREEN + '====================================================================')
    print(Style.RESET_ALL)

    #################################################################################
    # Ввод площади объекта, кв.м.
    print 'Введите площадь объекта, кв.м.: ',
    building_area = input()

    # Ввод стоимости права аренды, руб в год
    print 'Введите стоимость права аренды, руб/год: ',
    rent_rights_cost = input()

    #################################################################################
    # Вывод постоянных пораметров из конфигурационного файла
    if config.PRINT_CONFIG_FLAG:
        print '\n-------------------------------------------------'

        print "Средняя стоимость аренды в месяц: {0} руб".format(config.AVERAGE_RENTAL)
        print "Количество доходных месяцев в году: {0}".format(config.PROFIT_MONTHS)
        print "Стоимость предварительного ремонта за 1 кв.м.: {0}".format(config.REPAIR)

        print "Стоимость регистрации договора: {0} руб".format(config.CONTRACT_REGISTRATION)
        print "Мелкие расходы на запуск объекта: {0} руб".format(config.RUNNING_COST)

        print "Стоимость отопления в месяц: {0} руб".format(config.HEATING)
        print "Обслуживание ЖЭКом в месяц: {0} руб".format(config.HOUSING_OFFICE)
        print "Минимальная страховка за 1 кв.м. в месяц: {0} руб".format(config.MIN_INSURANCE)
        print "Бухгалтерское обслуживание в месяц: {0} руб".format(config.ACCOUNTING_SERVICE)

        print "Требуемый коэффициент доходности: {0}".format(config.REQUIRED_PROFIT_MARGIN)

    #################################################################################
    # *** Расчёт неосновных параметров ***
    # Страховка всей площади, руб в месяц
    all_area_insurance = building_area * config.MIN_INSURANCE

    print '\n-------------------------------------------------'
    print('Страховка всей площади: {0} руб/мес'.format(all_area_insurance))

    #################################################################################
    # *** Расчёт основных параметров ***
    # Доход от аренды в месяц
    month_rental_income = building_area * config.AVERAGE_RENTAL

    # Доход в год с учётом несдаваемых месяцев
    year_rental_income = building_area * config.AVERAGE_RENTAL * config.PROFIT_MONTHS

    print '\n-------------------------------------------------'
    print('Доход от аренды в месяц: {0} руб/мес'.format(month_rental_income))
    print('Доход от аренды в год (за {0} месяцев): {1} руб'
          .format(config.PROFIT_MONTHS, year_rental_income))

    #################################################################################


if __name__ == '__main__':
    main()
