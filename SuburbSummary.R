data=read.csv("C:/Users/marcn/Google Drive/Coding things/Webscraping/Real Estate/results 17_4_2019.csv")
View(data)
dim(data) # check data dimension
names(data[, 1:5]) # names of the first 5 columns
data[1,5]
data[1,5]
data[1,5]+data[2,5]
prices = data[,5]
summary(prices)
?subset
  
Brunswick = subset(data,suburb=="Brunswick")
View(Brunswick)
levels(data[1,1])
for (burb in levels(data[1,1])){
  assign(burb,subset(data,suburb==burb))
  #variable<-as.name(burb)
  #burb=subset(data,suburb==burb)
}
summary(Brunswick[,5])
View(Abbotsford)
Abbotsford[,5]
mean(na.omit(Abbotsford[,5]))
for (burb in levels(data[1,1])){
  print(paste("The average sale price in ", burb, " was $",mean(na.omit(eval(parse(text=burb))[,5])), sep=""))
}

