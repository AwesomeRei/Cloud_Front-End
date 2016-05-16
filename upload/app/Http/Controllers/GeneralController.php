<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Response;

class GeneralController extends Controller {

	public function index(Request $request) {
		$uploadedFile = $request->file('image');

		$pathPicture = $uploadedFile->getClientOriginalName();

		if ($uploadedFile->move(base_path() . '/public/images/web/', $pathPicture)) {

			return Response::json(['status' => 1], 200);
		} else {

			return Response::json(['status' => 0], 400);
		}

	}

}
