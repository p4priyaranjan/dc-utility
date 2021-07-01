from django.db import models

# Create your models here.
class TotalEntry(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    district_name = models.TextField(blank=True, null=True)
    loc_name = models.TextField(blank=True, null=True)
    dc_name = models.TextField(blank=True, null=True)
    day1sd = models.IntegerField(db_column='Day1SD', blank=True, null=True)  # Field name made lowercase.      
    day01fir = models.IntegerField(db_column='Day01FIR', blank=True, null=True)  # Field name made lowercase.  
    day02sd = models.IntegerField(db_column='Day02SD', blank=True, null=True)  # Field name made lowercase.    
    day02fir = models.IntegerField(db_column='Day02FIR', blank=True, null=True)  # Field name made lowercase.  
    day03sd = models.IntegerField(db_column='Day03SD', blank=True, null=True)  # Field name made lowercase.    
    day03fir = models.IntegerField(db_column='Day03FIR', blank=True, null=True)  # Field name made lowercase.  
    day04sd = models.IntegerField(db_column='Day04SD', blank=True, null=True)  # Field name made lowercase.    
    day04fir = models.IntegerField(db_column='Day04FIR', blank=True, null=True)  # Field name made lowercase.  
    day05sd = models.IntegerField(db_column='Day05SD', blank=True, null=True)  # Field name made lowercase.    
    day05fir = models.IntegerField(db_column='Day05FIR', blank=True, null=True)  # Field name made lowercase.  
    day06sd = models.IntegerField(db_column='Day06SD', blank=True, null=True)  # Field name made lowercase.    
    day06fir = models.IntegerField(db_column='Day06FIR', blank=True, null=True)  # Field name made lowercase.  
    day07sd = models.IntegerField(db_column='Day07SD', blank=True, null=True)  # Field name made lowercase.    
    day07fir = models.IntegerField(db_column='Day07FIR', blank=True, null=True)  # Field name made lowercase.  
    day08sd = models.IntegerField(db_column='Day08SD', blank=True, null=True)  # Field name made lowercase.    
    day08fir = models.IntegerField(db_column='Day08FIR', blank=True, null=True)  # Field name made lowercase.  
    day09sd = models.IntegerField(db_column='Day09SD', blank=True, null=True)  # Field name made lowercase.    
    day09fir = models.IntegerField(db_column='Day09FIR', blank=True, null=True)  # Field name made lowercase.  
    day10sd = models.IntegerField(db_column='Day10SD', blank=True, null=True)  # Field name made lowercase.    
    day10fir = models.IntegerField(db_column='Day10FIR', blank=True, null=True)  # Field name made lowercase.  
    day11sd = models.IntegerField(db_column='Day11SD', blank=True, null=True)  # Field name made lowercase.    
    day11fir = models.IntegerField(db_column='Day11FIR', blank=True, null=True)  # Field name made lowercase.  
    day12sd = models.IntegerField(db_column='Day12SD', blank=True, null=True)  # Field name made lowercase.    
    day12fir = models.IntegerField(db_column='Day12FIR', blank=True, null=True)  # Field name made lowercase.  
    day13sd = models.IntegerField(db_column='Day13SD', blank=True, null=True)  # Field name made lowercase.    
    day13fir = models.IntegerField(db_column='Day13FIR', blank=True, null=True)  # Field name made lowercase.  
    day14sd = models.IntegerField(db_column='Day14SD', blank=True, null=True)  # Field name made lowercase.    
    day14fir = models.IntegerField(db_column='Day14FIR', blank=True, null=True)  # Field name made lowercase.  
    day15sd = models.IntegerField(db_column='Day15SD', blank=True, null=True)  # Field name made lowercase.    
    day15fir = models.IntegerField(db_column='Day15FIR', blank=True, null=True)  # Field name made lowercase.  
    other_entry = models.IntegerField(db_column='Other_entry', blank=True, null=True)  # Field name made lowercase.
    perps = models.FloatField(blank=True, null=True)
    zeroday = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Total_Entry'
