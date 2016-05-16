<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Order extends Model
{
    protected $table = 'orders';

    protected $fillable =
        [   'design_id',
            'description',
            'designer_id',
            'customer_id',
            'status',
            'minbudget',
            'maxbudget',
            'timelimit'];

    public $timestamps = true;
    protected $softDeletes = true;
    public $incrementing = true;
    protected $dates = ['deleted_at'];
    protected $primaryKey = 'id';
    protected $hidden = ['password', 'remember_token'];

}
