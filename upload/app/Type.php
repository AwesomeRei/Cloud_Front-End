<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Type extends Model
{
    protected $fillable =
        [   'name',
            'description'];

    public $timestamps = false;
    protected $softDeletes = true;
    public $incrementing = true;
    protected $dates = ['deleted_at'];
    protected $primaryKey = 'id';

    public function designs(){
        return $this->hasMany('App\Design', 'type', 'id');
    }


}
