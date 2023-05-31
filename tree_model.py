def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/6194fa468be2aa39c0003f43

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 126):
        if (glucose > 157):
            if (bmi is None):
                return u'True'
            if (bmi > 29.32083):
                if (insulin is None):
                    return u'True'
                if (insulin > 629):
                    if (bmi > 33.4):
                        return u'False'
                    if (bmi <= 33.4):
                        return u'True'
                if (insulin <= 629):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.32366):
                        if (age is None):
                            return u'True'
                        if (age > 44):
                            if (pregnancies is None):
                                return u'True'
                            if (pregnancies > 6):
                                return u'True'
                            if (pregnancies <= 6):
                                if (age > 51):
                                    if (bmi > 45.05):
                                        return u'False'
                                    if (bmi <= 45.05):
                                        return u'True'
                                if (age <= 51):
                                    return u'False'
                        if (age <= 44):
                            return u'True'
                    if (diabetes_pedigree <= 0.32366):
                        if (bmi > 35.3):
                            if (bmi > 45.6):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 77):
                                    return u'True'
                                if (blood_pressure <= 77):
                                    return u'False'
                            if (bmi <= 45.6):
                                return u'True'
                        if (bmi <= 35.3):
                            if (glucose > 159):
                                if (glucose > 177):
                                    if (glucose > 192):
                                        return u'True'
                                    if (glucose <= 192):
                                        return u'False'
                                if (glucose <= 177):
                                    return u'True'
                            if (glucose <= 159):
                                return u'False'
            if (bmi <= 29.32083):
                if (blood_pressure is None):
                    return u'True'
                if (blood_pressure > 79):
                    return u'False'
                if (blood_pressure <= 79):
                    if (age is None):
                        return u'True'
                    if (age > 62):
                        return u'False'
                    if (age <= 62):
                        if (bmi > 25.85):
                            if (bmi > 27.9):
                                return u'True'
                            if (bmi <= 27.9):
                                if (blood_pressure > 69):
                                    return u'True'
                                if (blood_pressure <= 69):
                                    return u'False'
                        if (bmi <= 25.85):
                            return u'True'
        if (glucose <= 157):
            if (bmi is None):
                return u'False'
            if (bmi > 29.93):
                if (age is None):
                    return u'True'
                if (age > 30):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.43188):
                        if (age > 44):
                            return u'True'
                        if (age <= 44):
                            if (insulin is None):
                                return u'True'
                            if (insulin > 306):
                                return u'False'
                            if (insulin <= 306):
                                if (bmi > 40.05):
                                    if (bmi > 40.9):
                                        return u'True'
                                    if (bmi <= 40.9):
                                        return u'False'
                                if (bmi <= 40.05):
                                    return u'True'
                    if (diabetes_pedigree <= 0.43188):
                        if (bmi > 45.55):
                            return u'True'
                        if (bmi <= 45.55):
                            if (glucose > 130):
                                if (diabetes_pedigree > 0.1585):
                                    if (bmi > 32.45):
                                        if (glucose > 137):
                                            if (age > 42):
                                                if (diabetes_pedigree > 0.2265):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.2265):
                                                    return u'False'
                                            if (age <= 42):
                                                return u'False'
                                        if (glucose <= 137):
                                            return u'True'
                                    if (bmi <= 32.45):
                                        return u'False'
                                if (diabetes_pedigree <= 0.1585):
                                    return u'True'
                            if (glucose <= 130):
                                return u'False'
                if (age <= 30):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 61):
                        if (insulin is None):
                            return u'False'
                        if (insulin > 260):
                            return u'False'
                        if (insulin <= 260):
                            if (bmi > 41.7):
                                if (blood_pressure > 85):
                                    return u'True'
                                if (blood_pressure <= 85):
                                    if (bmi > 42.7):
                                        return u'False'
                                    if (bmi <= 42.7):
                                        return u'True'
                            if (bmi <= 41.7):
                                if (blood_pressure > 73):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 4):
                                        return u'True'
                                    if (pregnancies <= 4):
                                        return u'False'
                                if (blood_pressure <= 73):
                                    if (bmi > 32.45):
                                        if (bmi > 33.75):
                                            if (blood_pressure > 65):
                                                if (glucose > 129):
                                                    return u'True'
                                                if (glucose <= 129):
                                                    return u'False'
                                            if (blood_pressure <= 65):
                                                return u'False'
                                        if (bmi <= 33.75):
                                            return u'False'
                                    if (bmi <= 32.45):
                                        return u'True'
                    if (blood_pressure <= 61):
                        if (glucose > 127):
                            return u'True'
                        if (glucose <= 127):
                            return u'False'
            if (bmi <= 29.93):
                if (glucose > 145):
                    if (age is None):
                        return u'False'
                    if (age > 40):
                        return u'True'
                    if (age <= 40):
                        if (bmi > 28.45):
                            return u'False'
                        if (bmi <= 28.45):
                            if (bmi > 26.35):
                                return u'True'
                            if (bmi <= 26.35):
                                return u'False'
                if (glucose <= 145):
                    if (insulin is None):
                        return u'False'
                    if (insulin > 132):
                        return u'False'
                    if (insulin <= 132):
                        if (bmi > 28.15):
                            if (bmi > 28.55):
                                if (glucose > 135):
                                    return u'False'
                                if (glucose <= 135):
                                    return u'True'
                            if (bmi <= 28.55):
                                return u'True'
                        if (bmi <= 28.15):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 73):
                                return u'False'
                            if (blood_pressure <= 73):
                                if (diabetes_pedigree is None):
                                    return u'False'
                                if (diabetes_pedigree > 0.437):
                                    return u'False'
                                if (diabetes_pedigree <= 0.437):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 5):
                                        return u'False'
                                    if (pregnancies <= 5):
                                        if (bmi > 23.45):
                                            return u'True'
                                        if (bmi <= 23.45):
                                            return u'False'
    if (glucose <= 126):
        if (bmi is None):
            return u'False'
        if (bmi > 26.43324):
            if (age is None):
                return u'False'
            if (age > 28):
                if (glucose > 99):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.56888):
                        if (pregnancies is None):
                            return u'True'
                        if (pregnancies > 6):
                            return u'True'
                        if (pregnancies <= 6):
                            if (age > 30):
                                if (bmi > 33.05):
                                    if (diabetes_pedigree > 1.276):
                                        return u'True'
                                    if (diabetes_pedigree <= 1.276):
                                        return u'False'
                                if (bmi <= 33.05):
                                    if (blood_pressure is None):
                                        return u'True'
                                    if (blood_pressure > 69):
                                        return u'True'
                                    if (blood_pressure <= 69):
                                        if (bmi > 27.2):
                                            return u'False'
                                        if (bmi <= 27.2):
                                            return u'True'
                            if (age <= 30):
                                return u'True'
                    if (diabetes_pedigree <= 0.56888):
                        if (age > 54):
                            return u'False'
                        if (age <= 54):
                            if (diabetes_pedigree > 0.19888):
                                if (pregnancies is None):
                                    return u'True'
                                if (pregnancies > 0):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 11):
                                        if (pregnancies > 1):
                                            if (pregnancies > 8):
                                                if (skinfold is None):
                                                    return u'False'
                                                if (skinfold > 32):
                                                    return u'False'
                                                if (skinfold <= 32):
                                                    return u'True'
                                            if (pregnancies <= 8):
                                                return u'False'
                                        if (pregnancies <= 1):
                                            if (bmi > 33.25):
                                                return u'True'
                                            if (bmi <= 33.25):
                                                return u'False'
                                    if (insulin <= 11):
                                        if (blood_pressure is None):
                                            return u'True'
                                        if (blood_pressure > 81):
                                            if (bmi > 41.4):
                                                return u'True'
                                            if (bmi <= 41.4):
                                                return u'False'
                                        if (blood_pressure <= 81):
                                            if (diabetes_pedigree > 0.378):
                                                if (glucose > 105):
                                                    if (bmi > 29.9):
                                                        return u'False'
                                                    if (bmi <= 29.9):
                                                        if (pregnancies > 8):
                                                            return u'False'
                                                        if (pregnancies <= 8):
                                                            return u'True'
                                                if (glucose <= 105):
                                                    return u'True'
                                            if (diabetes_pedigree <= 0.378):
                                                if (diabetes_pedigree > 0.2585):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.2585):
                                                    if (bmi > 34.1):
                                                        return u'False'
                                                    if (bmi <= 34.1):
                                                        if (pregnancies > 8):
                                                            return u'False'
                                                        if (pregnancies <= 8):
                                                            return u'True'
                                if (pregnancies <= 0):
                                    return u'True'
                            if (diabetes_pedigree <= 0.19888):
                                if (age > 34):
                                    if (glucose > 108):
                                        return u'True'
                                    if (glucose <= 108):
                                        if (age > 36):
                                            return u'False'
                                        if (age <= 36):
                                            return u'True'
                                if (age <= 34):
                                    return u'False'
                if (glucose <= 99):
                    if (diabetes_pedigree is None):
                        return u'False'
                    if (diabetes_pedigree > 0.796):
                        if (bmi > 41.1):
                            return u'False'
                        if (bmi <= 41.1):
                            return u'True'
                    if (diabetes_pedigree <= 0.796):
                        if (glucose > 94):
                            if (glucose > 97):
                                return u'False'
                            if (glucose <= 97):
                                if (bmi > 36.2):
                                    return u'False'
                                if (bmi <= 36.2):
                                    return u'True'
                        if (glucose <= 94):
                            if (pregnancies is None):
                                return u'False'
                            if (pregnancies > 11):
                                if (bmi > 31.25):
                                    return u'False'
                                if (bmi <= 31.25):
                                    return u'True'
                            if (pregnancies <= 11):
                                return u'False'
            if (age <= 28):
                if (bmi > 30.51369):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 37):
                        if (insulin is None):
                            return u'False'
                        if (insulin > 172):
                            return u'False'
                        if (insulin <= 172):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.48765):
                                if (glucose > 124):
                                    return u'True'
                                if (glucose <= 124):
                                    if (bmi > 32.66667):
                                        if (blood_pressure > 61):
                                            if (bmi > 34.85):
                                                if (blood_pressure > 63):
                                                    if (pregnancies is None):
                                                        return u'False'
                                                    if (pregnancies > 1):
                                                        if (blood_pressure > 64):
                                                            if (diabetes_pedigree > 0.531):
                                                                if (bmi > 42.8):
                                                                    if (bmi > 43.7):
                                                                        return u'False'
                                                                    if (bmi <= 43.7):
                                                                        return u'True'
                                                                if (bmi <= 42.8):
                                                                    return u'False'
                                                            if (diabetes_pedigree <= 0.531):
                                                                return u'True'
                                                        if (blood_pressure <= 64):
                                                            return u'True'
                                                    if (pregnancies <= 1):
                                                        return u'False'
                                                if (blood_pressure <= 63):
                                                    return u'True'
                                            if (bmi <= 34.85):
                                                return u'True'
                                        if (blood_pressure <= 61):
                                            return u'False'
                                    if (bmi <= 32.66667):
                                        return u'False'
                            if (diabetes_pedigree <= 0.48765):
                                if (bmi > 45.35):
                                    return u'True'
                                if (bmi <= 45.35):
                                    if (diabetes_pedigree > 0.28558):
                                        return u'False'
                                    if (diabetes_pedigree <= 0.28558):
                                        if (blood_pressure > 55):
                                            if (skinfold is None):
                                                return u'False'
                                            if (skinfold > 30):
                                                return u'False'
                                            if (skinfold <= 30):
                                                if (blood_pressure > 72):
                                                    if (bmi > 33.95):
                                                        if (diabetes_pedigree > 0.2225):
                                                            return u'True'
                                                        if (diabetes_pedigree <= 0.2225):
                                                            return u'False'
                                                    if (bmi <= 33.95):
                                                        return u'True'
                                                if (blood_pressure <= 72):
                                                    return u'False'
                                        if (blood_pressure <= 55):
                                            if (blood_pressure > 47):
                                                return u'True'
                                            if (blood_pressure <= 47):
                                                return u'False'
                    if (blood_pressure <= 37):
                        return u'True'
                if (bmi <= 30.51369):
                    if (pregnancies is None):
                        return u'False'
                    if (pregnancies > 7):
                        return u'True'
                    if (pregnancies <= 7):
                        return u'False'
        if (bmi <= 26.43324):
            if (diabetes_pedigree is None):
                return u'False'
            if (diabetes_pedigree > 0.6545):
                if (bmi > 23):
                    return u'False'
                if (bmi <= 23):
                    if (bmi > 22.3):
                        return u'True'
                    if (bmi <= 22.3):
                        return u'False'
            if (diabetes_pedigree <= 0.6545):
                return u'False'
