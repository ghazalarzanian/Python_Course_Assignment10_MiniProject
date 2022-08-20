import pytube
SEries=[]
FIlms=[]
DOcumentaries=[]
CLips=[]
ACtors=[]
NewCasts=[]
def Load():
    print('Loading...')
    myfile1= open('Main.txt','r')
    data1 = myfile1.read()
    Items_List=data1.split('\n')
    for i in range(len(Items_List)):
        ACtors.clear()
        Media_info=Items_List[i].split(',')
        if Media_info[0]=='Series':
            for i in range(8,len(Media_info),2):
                ACtors.append(Actor(Media_info[i],Media_info[i+1]))
            SEries.append(Series(Media_info[1],Media_info[2],Media_info[3],Media_info[4],Media_info[5],ACtors,Media_info[6],Media_info[7]))
            # for obj in ACtors:
            #     print("--------------------")
            #     obj.ShowActors()
        elif Media_info[0]=='Film':
            for i in range(6,len(Media_info),2):
                ACtors.append(Actor(Media_info[i],Media_info[i+1]))
            FIlms.append(Film(Media_info[1],Media_info[2],Media_info[3],Media_info[4],Media_info[5],ACtors))
        elif Media_info[0]=='Documantary':
            for i in range(7,len(Media_info),2):
                ACtors.append(Actor(Media_info[i],Media_info[i+1]))
            DOcumentaries.append(Documantary(Media_info[1],Media_info[2],Media_info[3],Media_info[4],Media_info[5],ACtors,Media_info[6]))
        elif Media_info[0]=='Clip':
            for i in range(6,len(Media_info,2)):
                ACtors.append(Actor(Media_info[i],Media_info[i+1]))
            CLips.append(Clips(Media_info[1],Media_info[2],Media_info[3],Media_info[4],Media_info[5],ACtors))

def Add():
    A=input('Is it a Film or Series or a Clip or a Documantary?')
    if A == 'Film':
        NewFilm=Film(None,None,None,None,None,None)
        NewFilm.AddNewItem()
        FIlms.append(NewFilm)
        print('--------------------------')
        print('Added')
    if A=='Series':
        NewSeries=Series(None,None,None,None,None,None,None,None)
        NewSeries.AddNewItem()
        NewSeries.AddNewseries()
        SEries.append(NewSeries)
        print('--------------------------')
        print('Added')
    if A=='Documantary':
        NewDoc=Documantary(None,None,None,None,None,None,None)
        NewDoc.AddNewItem()
        NewDoc.AddNewDoc()
        DOcumentaries.append(NewDoc)
        print('--------------------------')
        print('Added')
    if A=='Clip':
        NewClip=Clips(None,None,None,None,None,None)
        NewClip.AddNewItem()
        CLips.append(NewClip)
        print('--------------------------')
        print('Added')
def Edit():
    A=str(input('Is it a Film or Series or a Clip or a Documantary?'))
    B=str(input('Enter the Name:'))
    i=-1
    if A == 'Film':
        for obj in FIlms:
            i+=1
            if obj.Name==B:
                FIlms.pop(i)
                print('Enter New Infomation')
                NewFilm=Film(None,None,None,None,None,None)
                NewFilm.AddNewItem()
                FIlms.append(NewFilm)
                break
    if A == 'Series':
        for obj in SEries:
            i+=1
            if obj.Name==B:
                SEries.pop(i)
                print('Enter New Infomation')
                NewSeries=Series(None,None,None,None,None,None,None,None)
                NewSeries.AddNewItem()
                NewSeries.AddNewseries()
                SEries.append(NewSeries)
                break
    if A == 'Documantary':
        for obj in DOcumentaries:
            i+=1
            if obj.Name==B:
                DOcumentaries.pop(i)
                print('Enter New Infomation')
                NewDoc=Documantary(None,None,None,None,None,None,None)
                NewDoc.AddNewItem()
                NewDoc.AddNewDoc()
                DOcumentaries.append(NewDoc)
                break
    if A == 'Clip':
        for obj in CLips:
            i+=1
            if obj.Name==B:
                CLips.pop(i)
                print('Enter New Infomation')
                NewClip=Clips(None,None,None,None,None,None)
                NewClip.AddNewItem()
                CLips.append(NewClip)
                break
def Delete():
    A=input('Is it a Film or Series or a Clip or a Documantary?')
    B=input('Enter the Name:')
    i=-1
    if A == 'Film':
        for obj in FIlms:
            i+=1
            print(i)
            if obj.Name==B:
                FIlms.pop(i)
                break
    if A == 'Series':
        for obj in SEries:
            i+=1
            if obj.Name==B:
                SEries.pop(i)
                break
    if A == 'Documantary':
        for obj in DOcumentaries:
            i+=1
            if obj.Name==B:
                DOcumentaries.pop(i)
                break
    if A == 'Clip':
        for obj in CLips:
            i+=1
            if obj.Name==B:
                CLips.pop(i)
                break
def Search():
    A=input('Is it a Film or Series or a Clip or a Documantary?')
    B=input('Enter the Name:')
    if A == 'Film':
        for obj in FIlms:
            if obj.Name==B:
                obj.Show_info()
                break
    if A == 'Series':
        for obj in SEries:
            if obj.Name==B:
                obj.Show_info()
                print('Season:',obj.Season)
                print('Epispde'.obj.Episode)
                print('---------------------')
                break
    if A=='Documantary':
        for obj in DOcumentaries:
            if obj.Name==B:
                obj.Show_info()
                print('Genre:',obj.Genre)
                print('--------------------')
                break
    if A=='Clips':
        for obj in CLips:
            if obj.Name==B:
                obj.Show_info()  
                break
def Download():
    A=input('Is it a Film or Series or a Clip or a Documantary?')
    B=input('Enter the Name:')
    if A == 'Film':
        for obj in FIlms:
            if obj.Name==B:
                link=obj.URL
                first_stream=pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./',filename='Film.mp4')
                break
    if A == 'Series':
        for i in SEries:
            if obj.Name==B:
                link=obj.URL
                first_stream=pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./',filename='Series.mp4')
                break
    if A=='Documantary':
        for obj in DOcumentaries:
            if obj.Name==B:
                link=obj.URL
                first_stream=pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./',filename='Documantry.mp4')
                break
    if A=='Clips':
        for obj in CLips:
            if obj.Name==B:
                link=obj.URL
                first_stream=pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./',filename='Clip.mp4')
                break
def Advanced_Search():
    Temp=[]
    A=int(input("Enter first Time:"))
    B=int(input('Enter second Time:'))
    for obj in FIlms:
        if int(obj.Duration) >= A and int(obj.Duration) <=B:
            Temp.append(obj.Name)
    for obj in SEries:
        if int(obj.Duration) >= A and int(obj.Duration) <=B:
            Temp.append(obj.Name)
    for obj in DOcumentaries:
        if int(obj.Duration) >= A and int(obj.Duration) <=B:
            Temp.append(obj.Name)
    for obj in CLips:
        if int(obj.Duration) >= A and int(obj.Duration) <=B:
            Temp.append(obj.Name)
    print(Temp)
def Exitt():
    ##FILM
    myfile=open('Films.txt','w')
    i=0
    for obj in FIlms:
        i+=1
        row=str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(len(FIlms)):
            myfile.write('\n')
    myfile.close()
    ##SERIES
    myfile=open('Series.txt','w')
    i=0
    for obj in SEries:
        i+=1
        row=str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)+','+str(obj.Season)+','+str(obj.Episode)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(len(SEries)):
            myfile.write('\n')
    myfile.close()
    ###DOCUMANTARIES
    myfile=open('Documentaries.txt','w')
    i=0
    for obj in DOcumentaries:
        i+=1
        row=str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)+','+str(obj.Genre)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(len(FIlms)):
            myfile.write('\n')
    myfile.close()
    ###CLIPS
    myfile=open('Clips.txt','w')
    i=0
    for obj in CLips:
        i+=1
        row=str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(len(CLips)):
            myfile.write('\n')
    myfile.close()
    ##MAIN
    myfile=open('Main.txt','w')
    Total=len(SEries)+len(FIlms)+len(CLips)+len(DOcumentaries)
    i=0
    for obj in SEries:
        i+=1
        row='Series'+','+str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)+','+str(obj.Season)+','+str(obj.Episode)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(Total):
            myfile.write('\n')
    for obj in FIlms:
        i+=1
        row='Film'+','+str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(Total):
            myfile.write('\n')
    for obj in DOcumentaries:
        i+=1
        row='Documantary'+','+str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)+','+str(obj.Genre)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(Total):
            myfile.write('\n')
    for obj in CLips:
        i+=1
        row='Clips'+','+str(obj.Name)+','+str(obj.Director)+','+str(obj.IMDB_Score)+','+str(obj.URL)+','+str(obj.Duration)
        for actor in obj.Casts:
            Actors=(str(actor.Name)+','+str(actor.Family))
            row=row+','+Actors
        myfile.write(row)
        if i!=(Total):
            myfile.write('\n')
    myfile.close()
    exit()

def show():
    Choice=int()
    print('1-Add')
    print('2-Edit')
    print('3-Delete')
    print('4-Search')
    print('5-Show List')
    print('6-Download')
    print('7-Advanced Search')
    print('8-Exit and Save')
    Choice=int(input("Enter your Choice:"))
    if Choice==1:
        Add()
    if Choice==2:
        Edit()
    if Choice==3:
        Delete()
    if Choice==4:
        Search()
    if Choice==5:
        f = open("Main.txt", "r")
        print(f.read())
    if Choice==6:
        Download()
    if Choice==7:
        Advanced_Search()
    if Choice==8:
        Exitt()
class Media:
    def __init__(self,name,director,IMDB,url,duration,casts):
        self.Name=name
        self.Director=director
        self.IMDB_Score=IMDB
        self.URL=url
        self.Duration=duration
        self.Casts=[]
        if casts!=None:
            for obj in casts:
                self.Casts.append(Actor(obj.Name,obj.Family))
    def Show_info(self):
        print('------------------------------------')
        print(self.Name)
        print(self.Director)
        print(self.IMDB_Score)
        print(self.URL)
        print(self.Duration)
        for obj in self.Casts:
            obj.ShowActors()
        print('------------------------------------')
    def AddNewItem(self):
        self.Name=input("Enter the Name:")
        self.Director=input("Enter name of the Director:")
        self.IMDB_Score=input('Enter IMDB score:')
        self.URL=input("Enter URL :")
        self.Duration=input('Enter Duration in Min:')
        Count=int(input("Enter Number of casts:"))
        NewCasts.clear()
        for i in range(Count):
            print("Enter Name of Cast Number",i+1,':')
            Name=input()
            print("Enter Family of Cast Number",i+1,':')
            Family=input()
            self.Casts.append(Actor(Name,Family))
class Film(Media):
    def __init__(self, name, director, IMDB, url, duration, casts):
        Media.__init__(self,name, director, IMDB, url, duration, casts)
class Series(Media):
    def __init__(self, name, director, IMDB, url, duration, casts,season,episode):
        Media.__init__(self,name, director, IMDB, url, duration, casts)
        self.Season=season
        self.Episode=episode
    def AddNewseries(self):
        self.Season=input("Enter Number of Seasons:")
        self.Episode=input("Enter Number of Episodes for each season:")
class Documantary(Media):
    def __init__(self, name, director, IMDB, url, duration, casts,genre):
        Media.__init__(self,name, director, IMDB, url, duration, casts)
        self.Genre=genre
    def AddNewDoc(self):
        self.Genre=input("Enter the Genre:")
class Clips(Media):
    def __init__(self, name, director, IMDB, url, duration, casts):
        Media.__init__(self,name, director, IMDB, url, duration, casts)
class Actor():
    def __init__(self,n,f):
        self.Name=n
        self.Family=f
    def ShowActors(self):
        print(self.Name,self.Family)
##############################
Load()
while True:
    show()