<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Role extends Model
{
    protected $table = 'roles';

    protected $fillable =
        [ 'name'];

    public $timestamps = true;
    protected $softDeletes = true;
    public $incrementing = true;
    protected $dates = ['deleted_at'];
    protected $primaryKey = 'id';

    public function user(){
        $this->hasMany('App\User', 'role', 'id');
    }
}
