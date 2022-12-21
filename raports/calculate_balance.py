from .models import Sen_equip, Balance
from .forms import BalanceForm

from datetime import datetime,timedelta, date
from django.utils import timezone


def calculate_balance(request, form_balance):
    items_tech = Sen_equip.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1]
    items_balance = Balance.objects.all().order_by('-id')[:1]
    values_tech = items_tech.values()
    values_balans = items_balance.values()
    print(items_tech.values())
    print(values_balans.values())
    yestarday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    print(yestarday)

    items_balance_yesterday =  Balance.objects.filter(date_update__contains= yestarday).order_by('-id')[:1]
    print(items_balance_yesterday.values()) 
    values_balans_yesterday = items_balance_yesterday.values()
    
    tag_a = float(values_balans_yesterday[0]['par_aa'])
    tag_b = float(values_balans_yesterday[0]['par_bb'])
    tag_c = float(values_balans_yesterday[0]['par_cc'])
    print("A: ", tag_a,"B: ", tag_b,"C: ", tag_c)

    """Приход товарного МЭГ (100% мас.) на склад фКГДУ(поз.6)"""
    # tag_d = float(values_balans[0]['par_d'])
    tag_d = float(form_balance['par_d'].value())
    """Приход товарного МЭГ 100% со склада ПБ на склад УКПГ(поз.20)"""
    # tag_e = float(values_balans[0]['par_e'])
    tag_e = float(form_balance['par_e'].value())
    """Вовлечение тованого МЭГ со склада УКПГ(поз.20)"""
    # tag_f = float(values_balans[0]['par_f'])
    tag_f = float(form_balance['par_f'].value())

    """Концентрация МЭГ"""
    # tag_g_nmag = float(values_balans[0]['par_g_nmag'])
    # tag_g_rmag_30i_1 = float(values_balans[0]['par_g_rmag_30i_1'])
    # tag_g_rmag_60e_1 = float(values_balans[0]['par_g_rmag_60e_1'])
    tag_g_nmag = float(form_balance['par_g_nmag'].value())
    tag_g_rmag_30i_1 = float(form_balance['par_g_rmag_30i_1'].value())
    tag_g_rmag_60e_1 = float(form_balance['par_g_rmag_60e_1'].value())

    """Плотность рМЭГ"""
    # tag_h = float(values_balans[0]['par_h'])
    tag_h = float(form_balance['par_h'].value())
    # print("D: ", tag_d,"E: ", tag_e,"F: ", tag_f,"G: ", par_g_nmag,"H: ", tag_h)

    """Приход рМЭГ"""
    tag_i = (float(values_tech[0]["r7"])+float(values_tech[0]["r8"])+float(values_tech[0]["r9"])) * 0.024

    """Регенерация рМэг из УРМ"""
    tag_j = (float(values_tech[0]["r10"])+float(values_tech[0]["r11"])+float(values_tech[0]["r12"])) * 0.024
    
    """Подача рМэг на ПДК"""
    tag_k = float(values_tech[0]["r18"]) * tag_h * 1.44

    # float(values_tech[0]["r20"]) = 0
    # float(values_tech[0]["r21"]) =0
    
    delta_epta = 0 + 0 + float(values_tech[0]["r22"]) + float(values_tech[0]["r23"]) + float(values_tech[0]["r24"]) + float(values_tech[0]["r25"]) + float(values_tech[0]["r26"]) + float(values_tech[0]["r27"])

    """Подача рМЭГ на скважину Р1"""
    tag_l = (0 + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р2"""
    tag_m = (0 + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р3"""
    tag_n = (float(values_tech[0]["r22"]) + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р4-бис"""
    tag_o = (float(values_tech[0]["r23"]) + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р5"""
    tag_p = (float(values_tech[0]["r24"]) + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р6"""
    tag_q = (float(values_tech[0]["r25"]) + tag_k) / delta_epta
    """Подача рМЭГ на скважину Р7"""
    tag_r = (float(values_tech[0]["r26"]) + tag_k) / delta_epta
    """Подача рМЭГ на манифольд"""
    tag_s = (float(values_tech[0]["r27"]) + tag_k) / delta_epta

    """Подача рМэг на технологию"""
    tag_t = float(values_tech[0]["r19"]) * tag_h * 1.44

    """Подача рМэг на площадку факельных сепараторов"""
    tag_u = float(values_tech[0]["r17"]) * tag_h * 1.44

    """Потери МЭГ на РЭН"""
    # tag_v = float(values_balans[0]['par_v'])
    tag_v = float(form_balance['par_v'].value())
    """КГС после УСК"""
    # tag_w = float(values_balans[0]['par_w'])
    tag_w = float(form_balance['par_w'].value()) 

    """Унос МЭГ с КГС (норма расхода 0.9495 кг/тонн)"""
    tag_x = (0.9495 * tag_w) / 1000

    """Остаток оборотного рМэг на конец суток"""
    tag_aa = (float(values_tech[0]['rt13'])+float(values_tech[0]['rt14'])+float(values_tech[0]['rt15'])+float(values_tech[0]['rt16'])) * tag_h
    
    """Остаток товарного МЭГ на поз.20 (100% мас.)"""
    tag_bb = tag_b + tag_e - tag_f

    """Остаток на конец суток на складе ПБ(100% мас.)"""
    tag_cc = tag_c + tag_d - tag_e

    save_Balance = Balance(par_a = tag_a ,       
    par_b = tag_b ,    
    par_c = tag_c ,    
    par_d = tag_d ,    
    par_e = tag_e ,    
    par_f = tag_f ,    
    par_g_nmag = tag_g_nmag ,
    par_g_rmag_30i_1 = tag_g_rmag_30i_1 ,
    par_g_rmag_60e_1 = tag_g_rmag_60e_1 ,    
    par_h = tag_h ,     
    par_i = tag_i ,     
    par_j  = tag_j ,    
    par_k  = tag_k ,    
    par_l  = tag_l ,    
    par_m = tag_m ,     
    par_n = tag_n ,     
    par_o = tag_o ,     
    par_p = tag_p ,     
    par_q = tag_q ,     
    par_r = tag_r ,     
    par_s = tag_s ,     
    par_t = tag_t ,     
    par_u = tag_u ,     
    par_v = tag_v ,     
    par_w = tag_w ,     
    par_x = tag_x ,     
    par_aa = tag_aa ,     
    par_bb = tag_bb ,    
    par_cc  = tag_cc ,    
    date_update = timezone.now())
    save_Balance.save()