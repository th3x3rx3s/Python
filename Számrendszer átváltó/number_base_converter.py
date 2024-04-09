def base_converter(num,ogbase,tgbase):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if ogbase<2 or ogbase>36 or tgbase<2 or tgbase>36:
        return "Hiba: Az eredeti és cél számrendszerek csak 2 és 36 között lehetnek."
    if num<0:
        return "Hiba: A szám nem lehet negatív."
    for x in str(num):
        if int(x)>=ogbase:
            return f"Hiba: {ogbase} alapú számrendszerben nem szerepelhet ilyen szám(0-{ogbase-1})."
    result=""
    if ogbase!=10 and tgbase!=10:
        #decimális számrendszerbe váltás
        n=len(str(num))-1
        decimal=0
        for x in range(len(str(num))):
            decimal+=(int(str(num)[x])*(ogbase**n))
            n=n-1
        #decimálisból cél számrendszerbe váltás
        while decimal>0:
            result+=digits[decimal%tgbase]
            decimal=decimal//tgbase
        return result[::-1]
    elif ogbase==10:
        #decimálisból cél számrendszerbe váltás
        while num>0:
            result+=digits[num%tgbase]
            num=num//tgbase
        return result[::-1]
    elif tgbase==10:
        #eredeti számrendszerből decimálisba váltás
        n=len(str(num))-1
        decimal=0
        for x in range(len(str(num))):
            decimal+=(int(str(num)[x])*(ogbase**n))
            n=n-1
        return decimal
    elif ogbase==tgbase:
        return num
