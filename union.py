from utils.db import ConnectDatabase

db = ConnectDatabase('ohop')

# sql = "select file_name, parse_number from union_yfyj_title;"
sql = "select build_company, house_project,house_position,house_use,will_sale_number," \
      "public_date,give_date,lottery_title from ohop_title;"

db.execute(sql)

# sql = "update students set name = '王铁蛋' where id = 6;"

for line in db.cursor.fetchall():
    print(line)

    wsn = line[4]

    bc = line[0]
    hp = line[1]
    hpo = line[2]
    hu = line[3]
    pd = line[5]
    gd = line[6]
    lt = line[7]

    sql = "update one_house_one_price set" \
          "  building_company='{}', house_project='{}', house_position='{}', " \
          "house_use='{}', public_date='{}', give_date='{}', lottery_title='{}'" \
          "where sale_number='{}';".format(bc, hp, hpo, hu, pd, gd, lt, wsn)

    db.run(sql)

    # print(sql)
