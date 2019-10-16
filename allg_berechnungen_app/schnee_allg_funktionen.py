
def berechnung_mue_wert(self,neigung):

    if 0 <= neigung < 15:
        mue_1 = 0.8
        mue_2 = 0.8
        mue_3 = 0.8+0.8*(neigung/30)


    elif 15 <= neigung <30:
        mue_1 = 0.8
        mue_2 = 0.8+0.2*((neigung-15)/15)
        mue_3 = 0.8+0.8*(neigung/30)


    elif 30<= neigung <60:
        mue_1 = 0.8*(60-neigung)/30
        mue_2 = 1.0*((60-neigung)/30)
        mue_3 = 1.6

    else:
        mue_1 = 0
        mue_2 = 0
        mue_3 = 1.6

    mue_werte = [mue_1,mue_2,mue_3]
    return mue_werte
