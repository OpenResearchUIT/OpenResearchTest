from database import *


####################################
#         Fetchall tables         #
####################################

def fetchAllCatalogs():
    with engine.connect() as connection:
        query = 'SELECT idCatalog, CatalogName FROM openresearch.Catalog'
        results = connection.execute(query).fetchall()
    return results


def fetchAllTagCatergories():
    with engine.connect() as connection:
        query = """ SELECT * FROM openresearch.Catalog_has_TagCategory
                    JOIN openresearch.TagCategory
                    ON openresearch.Catalog_has_TagCategory.TagCategory_idTagCategory = openresearch.TagCategory.idTagCategory;"""
        results = connection.execute(query).fetchall()
    return results


def fetchAllTags():
    with engine.connect() as connection:
        query = 'SELECT * FROM openresearch.Tags'
        results = connection.execute(query).fetchall()
    return results


# def fetchAllDocumentsByUser():
#     query = """SELECT * FROM openresearch.Document
#                JOIN openresearch.User
#                ON openresearch.User.idUser = openresearch.Document.User_idUser;"""
#     results = engine.execute(query).fetchall()
#     return results


def fetchFiletableData():
    with engine.connect() as connection:
        query = 'SELECT * FROM openresearch.Metadata;'
        results = connection.execute(query).fetchall()
    return results


def fetchAccessRights():
    with engine.connect() as connection:
        query = 'SELECT * FROM openresearch.Access;'
        results = connection.execute(query).fetchall()
    return results

def fetchTagIDWhereNameEquals(nameVar):
    with engine.connect() as connection:
        query = text(f"""SELECT idTags FROM openresearch.Tags where TagName = '{nameVar}';""")
        results = connection.execute(query).fetchone()
        if results is None:
            return None
        else:
            return results[0]

def fetchAuthorIDWhereNameEquals(firstname, lastname):
    with engine.connect() as connection:
        query = text(f"""SELECT idAuthor FROM openresearch.Author WHERE Firstname = '{firstname}' AND Lastname = '{lastname}';""")
        results = connection.execute(query).fetchone()
        if results is None:
            return None
        else:
            return results[0]

####################################
#             INSERTS              #
####################################

def insertToCatalog(catalogName):
    # write the insert statement
    statement = text(f"""INSERT INTO openresearch.Catalog (CatalogName) VALUES ('{catalogName}');""")
    engine.execute(statement)

def insertDocument(sizeVar, mimetypeVar, filenameVar, documentVar):
    with engine.connect() as con:
        result = con.execute(text("INSERT INTO openresearch.Document (Size, Mimetype,Filename,Document) VALUES (:sizeVar,:mimetypeVar,:filenameVar, :documentVar) RETURNING idDocument;"),sizeVar=sizeVar,mimetypeVar=mimetypeVar,filenameVar=filenameVar,documentVar=documentVar)
        res = [i.idDocument for i in result][0] # Returns the id of the inserted document
        return res

def insertMeta(tittel, descr, created,catalogid,access,userid,docid):
    with engine.connect() as con:
        result = con.execute(text("INSERT INTO openresearch.Metadata (Title, Description, CreationDate, Catalog_idCatalog, Access_idAccess, User_idUser,Document_idDocument) VALUES (:tittel, :descr, :created, :catalogid,:access,:userid,:docid);"),tittel=tittel,descr=descr,created=created,catalogid=catalogid,access=access,userid=userid,docid=docid)

def insertToDocumentHasTags(idDoc, idTag):
    with engine.connect() as con:
        result = con.execute(text("INSERT INTO openresearch.Document_has_Tags (Document_idDocument, Tags_idTags) VALUES (:idDoc, :idTag);"),idDoc=idDoc,idTag=idTag)

def insertAuthor(last,first):
    with engine.connect() as con:
        result = con.execute(text("INSERT INTO openresearch.Author (Lastname, Firstname) VALUES (:last, :first);"),last=last,first=first)

def insertToDocumentHasAuthor(idDoc, idAuthor):
    with engine.connect() as con:
        result = con.execute(text("INSERT INTO openresearch.Document_has_Tags (Dokument_idDokument, Author_idAuthor) VALUES (:idDoc, :idAuthor);"),idDoc=idDoc,idAuthor=idAuthor)

####################################
#             TESTING              #
####################################

# Catalogs ------------------------------------------------------------------
#insertMeta('tittel', 'desc', '2022-04-02',1,1,1,9)
# print(fetchAllCatalogs())  # Fetch all catalog items
# insertToCatalog('Sporst')  # insert a catalog with name

# Catalog TagCategories
# print(fetchAllTagCatergories())

# Tags
# print(fetchAllTags())

# Documents

# print(fetchAllDocumentsByUser())
# test Haakon
# print(fetchAccessRights())

# boom = [i.CatalogName for i in fetchAllCatalogs()]
# print(boom)

#tutu = [i.AccesType for i in fetchAccessRights()]

#print(tutu)

#tup = [(str(i.idAccess),i.AccesType) for i in fetchAccessRights()]
#print(tup)