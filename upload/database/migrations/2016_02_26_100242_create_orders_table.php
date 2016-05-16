<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateOrdersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('design_id');
            $table->string('title');
            $table->mediumText('description')->nullable();
            $table->integer('designer_id');
            $table->integer('customer_id');
            $table->boolean('status')->default(false);
            $table->integer('minbudget');
            $table->integer('maxbudget');
            $table->datetime('timelimit');
            $table->softDeletes();
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
        Schema::drop('orders');
    }
}
