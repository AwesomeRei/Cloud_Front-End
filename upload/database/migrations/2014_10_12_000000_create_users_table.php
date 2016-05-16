<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->increments('id');
            $table->string('firstname');
            $table->string('lastname')->nullable();
            $table->string('address')->nullable();
            $table->integer('identitynumber');
            $table->string('password', 60);
            $table->tinyInteger('role');
            $table->string('email');
            $table->string('contact')->nullable();
            $table->boolean('gender')->default(false);
            $table->boolean('verified')->default(false);
            $table->boolean('available')->default(true);
            $table->softDeletes();
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('users');
    }
}
