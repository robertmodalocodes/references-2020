library(EBImage)
x <-readImage(system.file('images','shapes.png', package='EBImage'))
x <-x[110:312,1:130]
y <-bwlabel(x)
display(y, title='Binary')

#Unduh citra buah(cth:alpukat) dari internet,dan baca melalui R 
original_image <-readImage(file.choose())
display(original_image)
r = channel(original_image,"r")
g = channel(original_image,"g")
b = channel(original_image,"b")
new_image = 0.2126*r+0.7152*g+0.0722*b
display(new_image)


Dataimage <-new_image@.Data
Subdata1<-Dataimage[110:312,130:200]
display(Subdata1)
Subdata2<-Dataimage[c(1:40, 100:150, 350:400 ), c(1:40, 100:150, 250:300 )]
display(Subdata2)





#Unduh citra buah(cth:alpukat) dari internet,dan baca melalui R 
original_image2 <-readImage(file.choose())
display(original_image2)
rr = channel(original_image2,"r")
gg = channel(original_image2,"g")
bb = channel(original_image2,"b")
new_image2 = 0.2126*rr+0.7152*gg+0.0722*bb
display(new_image2)


Dataimage2 <-new_image2@.Data
Subdata3<-Dataimage2[110:312,130:200]
display(Subdata3)
Subdata4<-Dataimage2[c(1:40, 100:150, 350:400 ), c(1:40, 100:150, 250:300 )]
display(Subdata4)


Dataimage2 <-Dataimage2[1:dim(Dataimage)[1], 1:dim(Dataimage)[2]]
obs1 <-as.vector(t(Dataimage))
obs2 <-as.vector(t(Dataimage2))
obs_gabung <-rbind(obs1,obs2)
dataset_buah <-as.data.frame(obs_gabung)
klas<-c("alpokat", "apel")
dataset_buah_baru<-cbind(dataset_buah, klas)
 dim(dataset_buah_baru)
dataset_buah_baru[1,640001]
dataset_buah_baru[2,640001]
