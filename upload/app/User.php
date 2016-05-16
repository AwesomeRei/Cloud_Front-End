<?php

namespace App;

use Illuminate\Auth\Authenticatable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Auth\Passwords\CanResetPassword;
use Illuminate\Foundation\Auth\Access\Authorizable;
use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
use Illuminate\Contracts\Auth\Access\Authorizable as AuthorizableContract;
use Illuminate\Contracts\Auth\CanResetPassword as CanResetPasswordContract;

class User extends Model implements AuthenticatableContract,
                                    AuthorizableContract,
                                    CanResetPasswordContract
{
    use Authenticatable, Authorizable, CanResetPassword;

    protected $table = 'users';

    protected $fillable =
        [   'firstname',
            'lastname',
            'identitynumber',
            'contact',
            'address',
            'role',
            'email',
            'verified',
            'available',
            'gender'];

    public $timestamps = true;
    protected $softDeletes = true;
    public $incrementing = true;
    protected $dates = ['deleted_at'];
    protected $primaryKey = 'id';
    protected $hidden = ['password', 'remember_token'];

    public function isDesigner(){
        return $this->role == 2;
    }

    public function isFounder(){
        return $this->role == 1;
    }

    public function isAvailable(){
        return $this->available;
    }

    public function isVerified(){
        return $this->verified;
    }

    public function designs(){
        return $this->hasMany('App\Design', 'user_id');
    }

    public function orders(){
        return $this->hasMany('App\Order', 'designer_id');
    }

    public function customer(){
        return $this->hasMany('App\Order', 'customer_id','id');
    }

    public function role(){
        return $this->belongsTo('App\Role','role','id');
    }


}
