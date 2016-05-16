<?php

use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Model::unguard();
        $this->call('RoleSeeder');
        $this->call('UserSeeder');
        $this->call('TypeSeeder');
        $this->call('DesignSeeder');

        Model::reguard();
    }
}

class UserSeeder extends Seeder{
    public function run()
    {
        DB::table('users')->delete();
        DB::table('users')->insert([
            //founder
            [   'firstname' => 'Safitri',
                'lastname' => 'Nur Wulandari',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('safi'),
                'email' => 'safi@safi.com',
                'contact' => '081081081',
                'verified' => false,
                'role' => 1,
                'available'=> false ],
//                designer
            [   'firstname' => 'Gali',
                'lastname' => 'Raka Siwi',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('gali'),
                'email' => 'gali@gali.com',
                'contact' => '081081081',
                'verified' => true,
                'role' => 2,
                'available'=> true ],
            [   'firstname' => 'Faisal',
                'lastname' => '',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('faisal'),
                'email' => 'gali@gali.com',
                'contact' => '081081081',
                'verified' => true,
                'role' => 2,
                'available'=> true ],
            [   'firstname' => 'Robby',
                'lastname' => 'Suma Prayogata',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('robby'),
                'email' => 'gali@gali.com',
                'contact' => '081081081',
                'verified' => true,
                'role' => 2,
                'available'=> true ],
            [   'firstname' => 'Sapta',
                'lastname' => 'Sunusae',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('sapta'),
                'email' => 'gali@gali.com',
                'contact' => '081081081',
                'verified' => true,
                'role' => 2,
                'available'=> true ],
            //customer
            [   'firstname' => 'Raihana',
                'lastname' => 'Putri Utami',
                'identitynumber' => '0000000000000',
                'password' => bcrypt('safi'),
                'email' => 'safi@safi.com',
                'contact' => '081081081',
                'verified' => false,
                'role' => 3,
                'available'=> false ]
        ]);

    }
}
class RoleSeeder extends Seeder{
    public function run()
    {
        DB::table('roles')->delete();
        DB::table('roles')->insert([
            [ 'name'=> 'Founder' ],
            [ 'name'=> 'Desainer' ],
            [ 'name'=> 'Customer']
        ]);
    }
}
class TypeSeeder extends Seeder{

    public function run(){
        DB::table('types')->delete();
        DB::table('types')->insert([
           ['name'=> 'Poster', 'description'=> ''],
//            ['name'=> 'Video', 'description'=> ''],
//            ['name'=> '3D', 'description'=> ''],
            ['name'=> 'Banner', 'description'=> ''],
            ['name'=> 'Logo', 'description'=> ''],
            ['name'=> 'Vektor', 'description'=> '']
        ]);
    }
}

class DesignSeeder extends Seeder{

    public function run(){
        DB::table('designs')->delete();
        DB::table('designs')->insert([
            [   'user_id'=> '2', 'title'=> 'Outside Of Spectacle',
                'description' => '', 'type'=> '1', 'verified'=>1 ],
            [   'user_id'=> '2', 'title'=> 'Central Industrianl, Working Waterfront City',
                'description' => '', 'type'=> '1', 'verified'=>1 ],
            [   'user_id'=> '2', 'title'=> 'Site Plan',
                'description' => '', 'type'=> '1', 'verified'=>1 ],
            [   'user_id'=> '2', 'title'=> 'Renewable Generator Ship',
                'description' => '', 'type'=> '1', 'verified'=>1 ],


            [   'user_id'=> '3', 'title'=> 'Layanan Orientasi Siswa',
                'description' => '', 'type'=> '2', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Isra Miraj',
                'description' => '', 'type'=> '2', 'verified'=> 1],
            [   'user_id'=> '3', 'title'=> 'Animasi SMKN Surabaya',
                'description' => '', 'type'=> '3', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Clash of Clans Surabaya',
                'description' => '', 'type'=> '3', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Atom',
                'description' => '', 'type'=> '3', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Gajah Bajah',
                'description' => '', 'type'=> '3', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Faishal Putra Ramadhan',
                'description' => '', 'type'=> '3', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Desain Baju Indonesia',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Selamat hari Idul Adha',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Pahlawan Masa Depan',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Redraw Smekda',
                'description' => '', 'type'=> '4', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Three of Us',
                'description' => '', 'type'=> '4', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Bayu Dwi Arianto',
                'description' => '', 'type'=> '4', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Min Ladunna Ilma',
                'description' => '', 'type'=> '4', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Teddy Firmansyah',
                'description' => '', 'type'=> '4', 'verified'=> 1 ],


            [   'user_id'=> '4', 'title'=> 'Epsilon',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],

            [   'user_id'=> '5', 'title'=> 'EBDB',
                'description' => '', 'type'=> '2', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Kicot',
                'description' => '', 'type'=> '2', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Poster Sthapachare',
                'description' => '', 'type'=> '2', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Studi Tektonika',
                'description' => '', 'type'=> '2', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Bulak Mild House',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Analisis Lahan',
                'description' => '', 'type'=> '1', 'verified'=> 1 ],
            [   'user_id'=> '3', 'title'=> 'Neon Park Gym Resto',
                'description' => '', 'type'=> '1', 'verified'=> 1 ]
        ]);
    }
}