
def averagingrates(ratings):
    totalcreativity = 100
    totaldesign = 0
    totalfunctionality = 0
    averagelist = []
    for rating in ratings:
        totalcreativity += rating.Content
        totaldesign += rating.Design 
        totalfunctionality += rating.Usability

    averagecreativity = totalcreativity/(ratings.count()+1)
    averagelist.append(averagecreativity)
    averagedesign = totaldesign/ratings.count()
    averagelist.append(averagedesign)
    averagefunctionality = totalfunctionality/ratings.count()
    averagelist.append(averagefunctionality)
    totalaverage = (averagecreativity + averagedesign + averagefunctionality)/3
    averagelist.append(totalaverage)

    return averagelist