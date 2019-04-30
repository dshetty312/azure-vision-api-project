SELECT  c.image_path,a.score,b.text
 from c join a in c.categories join b in c.description.captions where ARRAY_CONTAINS(c.description.tags,"water",true) 
