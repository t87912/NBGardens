# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:06:19 2016

@author: user
"""

# Simply holds the SQL queries in a list
# First element of list is empty so list index starts at 1 - for simplicity
# Empty strings are where Mongo Queries are used instead

queries = ["",
           "SELECT e.idEmployee, e.firstName, e.lastName, round(SUM(p.sellPrice*op.quantity),2) as 'Total Sales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between '%s' and '%s' group by e.idEmployee desc limit 20", # 1
           "SELECT c.idCustomer, c.firstName, c.lastName, round(SUM(p.sellPrice*op.quantity),2) as 'Total Sales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Customer as c On o.cust_idCustomer = c.idCustomer where o.createDate between '%s' and '%s' group by c.idCustomer desc limit 20", # 2
           "SELECT c.idCustomer, c.firstName, c.lastName, round(SUM(p.sellPrice*op.quantity),2) as 'Total Sales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Customer as c On o.cust_idCustomer = c.idCustomer where o.createDate between '%s' and '%s' group by c.idCustomer having round(SUM(p.sellPrice*op.quantity),2) > %s order by 'Total Sales' desc", # 3
           "Select round(sum(p.sellPrice*op.quantity),2) as 'Total Sales', round(sum(p.buyPrice*op.quantity),2) as 'Total Cost' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct where o.createDate between '%s' and '%s'", # 4
           "Select p.idProduct, round((sum(p.sellPrice*op.Quantity) - sum(p.buyPrice*op.Quantity)),2) as 'Return on Investment' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct where o.createDate between '%s' and '%s' and p.idProduct = '%s' group by p.idProduct", # 5
           "SELECT AVG(DATEDIFF(createDate, deliveredDate)) FROM Purchase WHERE createDate BETWEEN '%s' AND '%s'", # 6
           "", # 7
           "", # 8
           "", # 9
           "", #10
           "", #11
           "SELECT amount FROM Product Where idProduct = '%s'", # 12
           "SELECT op.Pro_idProduct, Sum(op.quantity) From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase where o.createDate between '%s' and '%s' group by op.Pro_idProduct", # 13
           "SELECT e.idEmployee, o.createDate, round(SUM(p.sellPrice*op.quantity),2) as 'Sales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between '%s' and '%s' AND e.idEmployee = %s group by o.createDate DESC", # new 14
           "", #15
           "SELECT op.Pro_idProduct, ROUND(Sum(op.quantity)), p.amount From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On p.idProduct = op.Pro_idProduct where o.createDate between '%s' and '%s' group by op.Pro_idProduct" # 16
]








   