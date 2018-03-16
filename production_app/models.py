from django.db import models
from django.utils import timezone


class Machinery(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128, blank=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Machinery"
        verbose_name_plural="Machineries"


class Cluster(models.Model):
    clustername = models.CharField(verbose_name="Cluster", max_length=128, blank=False)
    
    def __str__(self):
        return self.clustername

    class Meta:
        verbose_name="Cluster"
    
    
class Network(models.Model):
    
    network_name = models.CharField(verbose_name='Name', max_length=128,blank=False)
    cluster = models.ForeignKey(Cluster, null=True)

    def __str__(self):
        return self.network_name

    class Meta:
        verbose_name  = "Network"
        verbose_name_plural = "Networks"




class Member(models.Model):
    
    mem_id = models.CharField(verbose_name='ID', max_length=128, blank=False)
    mem_name = models.CharField(verbose_name='Name', max_length=128, blank=False )
    mem_addresse = models.CharField(verbose_name='Addresse', max_length=128, blank=True)
    mem_phone = models.CharField(verbose_name='Phone', max_length=128, blank=True)
    mem_mobile = models.CharField(verbose_name='Mobile', max_length=128, blank=True)
    mem_fax = models.CharField(verbose_name='Fax', max_length=128, blank=True)
    mem_email = models.CharField(verbose_name='Email', max_length=128, blank=True)
    mem_contactperson = models.CharField(verbose_name= 'Contact Name', max_length = 128,blank=True)
    mem_typeofproduct = models.CharField(choices=[('leather', 'Leather'),('synthetic', 'Synthetic'),('textile', 'Textile')], verbose_name='Type',max_length = 32,blank=True)
    mem_shoestype = models.CharField(choices=[('gents', 'Gents Shoes'), ('ladies', 'Ladies Shoes'), ('kids', 'Kids Shoes'), ('leatherbag','Leather Bag'),('garment','Garment'),('gloves','Gloves'),('accessories','Accessories')],verbose_name='Product Catagory', max_length = 32,blank=True)
    network = models.ForeignKey(Network, verbose_name="Network", null=True)
    
    
    class Meta:
        verbose_name  ="Enterprise"
        verbose_name_plural ="Enterprises"
    
    def __str__(self):
        return self.mem_name
        
class ProductionPerPhase(models.Model):
    Member=models.ForeignKey(Member,verbose_name="Enterprise")
    year=models.IntegerField(verbose_name="year")
    phase=models.CharField(verbose_name="Phase", choices=[('1', 'Jan-Apr'),('2', 'May-Aug'),('3','Sep-Dec')],max_length=32)
    permanentmaleemployee = models.IntegerField(verbose_name = 'Permanent M. Emp',blank=False)
    permanentfemaleemployee = models.CharField(verbose_name = 'Permanent F. Emp', max_length=128,blank=False)
    tempmaleemployee = models.IntegerField(verbose_name = 'Temporary M. Emp',blank=False)
    tempfemaleemployee = models.CharField(verbose_name = 'Temporary F. Emp', max_length=128 ,blank=False)
    shoes=models.IntegerField(verbose_name="Shoes in Dozen",blank=True)
    price=models.FloatField(verbose_name="Price")
    



        
class MemberMachinery(models.Model):
    member=models.ForeignKey(Member)
    machinery=models.ForeignKey(Machinery)
    quantity=models.IntegerField(verbose_name="Quantity", blank=False)




        
    
    
    
 
"""
class unidocluster_membermachinery(osv.osv):
    _name  ='unidocluster.membermachinery'
    _description  ="member machinery"
    _columns  ={
        'machinery_id =fields.many2one('unidocluster.machinery','Machinery'),
        'unitcost =models.CharField(verbose_name = 'Unit Cost', max_length = 128),
        'qty =models.CharField(verbose_name = 'Qty', max_length = 128),
        'mem_machinary_id =fields.many2one('unidocluster.member','Member'),
        
    }
unidocluster_membermachinery()

class unidocluster_membermachineryleased(osv.osv):
    _name  ='unidocluster.membermachineryleased'
    _description  ="member machinery leased"
    _columns  ={
        'machinery_id =fields.many2one('unidocluster.machinery','Machinery'),
        'estimatedunitcost =models.CharField(verbose_name = 'Estimated Unit Cost', max_length = 128),
        'actualunitcost =models.CharField(verbose_name = 'Actual Unit Cost', max_length = 128),
        
        'qty =models.CharField(verbose_name = 'Qty', max_length = 128),
        
        'mem_machinary_id =fields.many2one('unidocluster.member','Member'),
        'ntk_machinary_id =fields.many2one('unidocluster.network','Member'),
        'loanstatus = fields.selection([('requested','Requested'),('received','Received'),('refused','Refused')],'Status',max_length = 32),
        
        
    }
unidocluster_membermachineryleased()

class unidocluster_financeloan(osv.osv):
    _name  ='unidocluster.financeloan'
    _description  ="Finance loan"
    _columns  ={
        
        'requestedloan =models.CharField(verbose_name = 'Requested Loan', max_length = 128),
        'actualunitcost =models.CharField(verbose_name = 'Actual Given', max_length = 128),
        'sourcebank =models.CharField(verbose_name = 'Source Bank',max_length = 128),
        'mem_finance_id =fields.many2one('unidocluster.member','Member'),
        'ntk_finance_id =fields.many2one('unidocluster.network','Member'),
        'loanstatus = fields.selection([('requested','Requested'),('received','Received'),('refused','Refused')],'Status',max_length = 32),
        
        
    }
unidocluster_financeloan()



class unidocluster_machinery(osv.osv):
    _name = "unidocluster.machinery"
    _description  ='Machinery'
    _columns  ={
        'machinery_id =models.CharField(verbose_name = 'Machinery',max_length = 128),  
        'Machinaries =fields.one2many('unidocluster.membermachinery','machinery_id','Machinaries')     
       
    }
    _rec_name = "machinery_id"
unidocluster_machinery()

class unidocluster_memberrawmaterialperdozen(osv.osv):
    _name  ='unidocluster.memberrawmaterialperdozen'
    _description  ="Raw materials per Dozen"
    _columns  ={
                
        'rawmaterial_id =fields.many2one('unidocluster.rawmaterialtype','Raw Material'),
        'unitcost =models.CharField(verbose_name = 'Unit Cost', max_length = 128),
        'qty =models.CharField(verbose_name = 'Qty', max_length = 128),
        'mem_rawmaterial_id =fields.many2one('unidocluster.member','Member'),
        'productperdozen_id =fields.many2one('unidocluster.producttype','Product'),
        
    }
unidocluster_memberrawmaterialperdozen()

class unidocluster_rawmaterialtype(osv.osv):
    _name = "unidocluster.rawmaterialtype"
    _description  ='Raw Material'
    _columns  ={
        'rawmaterial_id =models.CharField(verbose_name = 'Raw Material',max_length = 128),  
        'rawmaterials =fields.one2many('unidocluster.memberrawmaterialperdozen','rawmaterial_id','Raw Materials'),     
        'marketlinkmaterials =fields.one2many('unidocluster.rawmateriallinkage','rawmateriallink_id','Raw Materials')
    }
    _rec_name = 'rawmaterial_id'
unidocluster_rawmaterialtype()

class unidocluster_producttype(osv.osv):
    _name = "unidocluster.producttype"
    _description  ='Product Type'
    _columns  ={
        'product_id =models.CharField(verbose_name = 'Product',max_length = 128),  
        'products =fields.one2many('unidocluster.production','product_id','Products'), 
        'productsperdozen = fields.one2many('unidocluster.memberrawmaterialperdozen','productperdozen_id','Products'),    
            }
    _rec_name = 'product_id'
unidocluster_producttype()


class unidocluster_production(osv.osv):
    _name = 'unidocluster.production'
    _description  ="production"
    _columns  ={
        'prod_period =models.CharField(verbose_name = 'Period', max_length = 128),
        'mem_production_id =fields.many2one('unidocluster.member','Member'),
        'prod_temp_emp =models.CharField(verbose_name = 'Temp Emp', max_length = 128),
        'prod_perm_emp =models.CharField(verbose_name = 'Permanent Emp', max_length = 128),
        
        'prod_perm_emp_male =models.CharField(verbose_name = 'Perm. M Emp', max_length = 128),
        'prod_perm_emp_female =models.CharField(verbose_name = 'Perm. F Emp', max_length = 128),
        
        'prod_temp_emp_male =models.CharField(verbose_name = 'Temp. M Emp', max_length = 128),
        'prod_temp_emp_female =models.CharField(verbose_name = 'Temp. F Emp', max_length = 128),
        
        'prod_gents_shoes =fields.selection([('gents', 'Gents Shoes'),('ladies', 'Ladies Shoes'),('kids','Kids Shoes'),('leatherbag','Leather Bag'),('garment','Garment'),('gloves','Gloves'),('accessories','Accessories')],'Product Catagory', max_length = 32),
        'prod_qty =models.CharField(verbose_name = 'Qty',max_length = 128),
        #'prod_kids_shoes =models.CharField(verbose_name = 'Other', max_length = 128),
        'product_id =fields.many2one('unidocluster.producttype','Product'),
        
        }

unidocluster_production()

class unidocluster_training(osv.osv):
    _name = 'unidocluster.training'
    _description  ="Training"
    _columns  ={
        'tra_datestart =fields.date('Date Start'),
        'tra_dateend =fields.date('Date End'),
        
        'mem_training_id =fields.many2one('unidocluster.network','Network'),
        
        
        'tra_name =models.CharField(verbose_name = 'Training Title', max_length = 128),
        'no_participants =models.CharField(verbose_name = 'Number of participants', max_length = 128),
        }

unidocluster_training()

class unidocluster_exhibition(osv.osv):
    _name = 'unidocluster.exhibition'
    _description  ="exhibition"
    _columns  ={
        'exh_datestart =fields.date('Date Start'),
        'exh_dateend =fields.date('Date End'),
        
        'network_exhibition_id =fields.many2one('unidocluster.network','Network'),
        
        
        'exh_name =models.CharField(verbose_name = 'Exhibition Title', max_length = 128),
        
        }

unidocluster_exhibition()




"""
