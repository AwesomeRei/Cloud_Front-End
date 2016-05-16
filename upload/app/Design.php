<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Design extends Model
{
    protected $table = 'designs';

    protected $fillable =
        [   'name',
            'user_id',
            'type',
            'title',
            'description',
//            1->poster, 2->video, 3-> 3d, 4 -> website
            'checked'];

    public $timestamps = true;
    protected $softDeletes = true;
    public $incrementing = true;
    protected $dates = ['deleted_at'];
    protected $primaryKey = 'id';

    public function designers(){
        return $this->belongsTo('App\User', 'user_id');
    }

    public function types(){
        return $this->hasOne('App\Type', 'type');
    }

}
