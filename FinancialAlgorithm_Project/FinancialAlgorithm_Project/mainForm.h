#pragma once

//
// Created by 陳柏言 (Alex Chen), National Taiwan University, Dpt. of Finance
//

# include <string>
# include <iostream>
# include <cmath>
# include <vector>
# include <random>
# include <chrono>
# include <format>


namespace FinAlgoProject {
	using namespace std;
	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;


	/// <summary>
	/// mainForm 的摘要
	/// </summary>
	public ref class mainForm : public System::Windows::Forms::Form
	{
	public:
		mainForm(void)
		{
			InitializeComponent();
			//
			//TODO:  在此加入建構函式程式碼
			//

		}

	protected:
		/// <summary>
		/// 清除任何使用中的資源。
		/// </summary>
		~mainForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::GroupBox^ outputBox;
	private: System::Windows::Forms::GroupBox^ inputBox;


	private: System::Windows::Forms::Label^ label1;
	private: System::Windows::Forms::Label^ label8;
	private: System::Windows::Forms::Label^ label7;
	private: System::Windows::Forms::Label^ label6;
	private: System::Windows::Forms::Label^ label5;
	private: System::Windows::Forms::Label^ label4;
	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::Label^ label2;
	private: System::Windows::Forms::TextBox^ sims_tb;

	private: System::Windows::Forms::TextBox^ sigma_tb;


	private: System::Windows::Forms::TextBox^ q_tb;


	private: System::Windows::Forms::TextBox^ r_tb;


	private: System::Windows::Forms::TextBox^ T_tb;


	private: System::Windows::Forms::TextBox^ K_tb;


	private: System::Windows::Forms::TextBox^ St_tb;
	private: System::Windows::Forms::TextBox^ rep_tb;


	private: System::Windows::Forms::GroupBox^ lookback;
	private: System::Windows::Forms::TextBox^ n_lookback_tb;


	private: System::Windows::Forms::Label^ label11;
	private: System::Windows::Forms::TextBox^ StMax_tb;


	private: System::Windows::Forms::Label^ label10;
	private: System::Windows::Forms::TextBox^ StMin_tb;


	private: System::Windows::Forms::Label^ label9;
	private: System::Windows::Forms::GroupBox^ tree;
	private: System::Windows::Forms::TextBox^ layers_tb;


	private: System::Windows::Forms::Label^ label12;


	private: System::Windows::Forms::GroupBox^ average;
	private: System::Windows::Forms::Label^ label13;


	private: System::Windows::Forms::TextBox^ time_elapsed_tb;

	private: System::Windows::Forms::TextBox^ n_avg_prev_tb;

	private: System::Windows::Forms::TextBox^ n_avg_tb;

	private: System::Windows::Forms::TextBox^ StAve_tb;

	private: System::Windows::Forms::Label^ label16;
	private: System::Windows::Forms::Label^ label15;
	private: System::Windows::Forms::Label^ label14;
	private: System::Windows::Forms::Button^ calc;

	private: System::Windows::Forms::Label^ author;
	private: System::Windows::Forms::Label^ email;


	private: System::Windows::Forms::GroupBox^ call_put;
	private: System::Windows::Forms::RadioButton^ put;
	private: System::Windows::Forms::RadioButton^ call;
	private: System::Windows::Forms::GroupBox^ models;
	private: System::Windows::Forms::RadioButton^ US_CRR;
	private: System::Windows::Forms::RadioButton^ EU_CRR;
	private: System::Windows::Forms::RadioButton^ EU_MC;
private: System::Windows::Forms::RadioButton^ EU_avg_MC;
private: System::Windows::Forms::RadioButton^ EU_lb_MC;
private: System::Windows::Forms::Label^ label17;
private: System::Windows::Forms::Label^ outputString;
private: System::Windows::Forms::GroupBox^ MC;









	protected:

	private:
		/// <summary>
		/// 設計工具所需的變數。
		/// </summary>
		System::ComponentModel::Container^ components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
		/// 這個方法的內容。
		/// </summary>
		void InitializeComponent(void)
		{
			this->outputBox = (gcnew System::Windows::Forms::GroupBox());
			this->outputString = (gcnew System::Windows::Forms::Label());
			this->inputBox = (gcnew System::Windows::Forms::GroupBox());
			this->MC = (gcnew System::Windows::Forms::GroupBox());
			this->rep_tb = (gcnew System::Windows::Forms::TextBox());
			this->sims_tb = (gcnew System::Windows::Forms::TextBox());
			this->label8 = (gcnew System::Windows::Forms::Label());
			this->label7 = (gcnew System::Windows::Forms::Label());
			this->tree = (gcnew System::Windows::Forms::GroupBox());
			this->layers_tb = (gcnew System::Windows::Forms::TextBox());
			this->label12 = (gcnew System::Windows::Forms::Label());
			this->call_put = (gcnew System::Windows::Forms::GroupBox());
			this->put = (gcnew System::Windows::Forms::RadioButton());
			this->call = (gcnew System::Windows::Forms::RadioButton());
			this->average = (gcnew System::Windows::Forms::GroupBox());
			this->time_elapsed_tb = (gcnew System::Windows::Forms::TextBox());
			this->n_avg_prev_tb = (gcnew System::Windows::Forms::TextBox());
			this->n_avg_tb = (gcnew System::Windows::Forms::TextBox());
			this->StAve_tb = (gcnew System::Windows::Forms::TextBox());
			this->label16 = (gcnew System::Windows::Forms::Label());
			this->label15 = (gcnew System::Windows::Forms::Label());
			this->label14 = (gcnew System::Windows::Forms::Label());
			this->label13 = (gcnew System::Windows::Forms::Label());
			this->lookback = (gcnew System::Windows::Forms::GroupBox());
			this->label17 = (gcnew System::Windows::Forms::Label());
			this->n_lookback_tb = (gcnew System::Windows::Forms::TextBox());
			this->label11 = (gcnew System::Windows::Forms::Label());
			this->StMax_tb = (gcnew System::Windows::Forms::TextBox());
			this->label10 = (gcnew System::Windows::Forms::Label());
			this->StMin_tb = (gcnew System::Windows::Forms::TextBox());
			this->label9 = (gcnew System::Windows::Forms::Label());
			this->sigma_tb = (gcnew System::Windows::Forms::TextBox());
			this->q_tb = (gcnew System::Windows::Forms::TextBox());
			this->r_tb = (gcnew System::Windows::Forms::TextBox());
			this->T_tb = (gcnew System::Windows::Forms::TextBox());
			this->K_tb = (gcnew System::Windows::Forms::TextBox());
			this->St_tb = (gcnew System::Windows::Forms::TextBox());
			this->label6 = (gcnew System::Windows::Forms::Label());
			this->label5 = (gcnew System::Windows::Forms::Label());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->calc = (gcnew System::Windows::Forms::Button());
			this->author = (gcnew System::Windows::Forms::Label());
			this->email = (gcnew System::Windows::Forms::Label());
			this->models = (gcnew System::Windows::Forms::GroupBox());
			this->EU_avg_MC = (gcnew System::Windows::Forms::RadioButton());
			this->EU_lb_MC = (gcnew System::Windows::Forms::RadioButton());
			this->US_CRR = (gcnew System::Windows::Forms::RadioButton());
			this->EU_CRR = (gcnew System::Windows::Forms::RadioButton());
			this->EU_MC = (gcnew System::Windows::Forms::RadioButton());
			this->outputBox->SuspendLayout();
			this->inputBox->SuspendLayout();
			this->MC->SuspendLayout();
			this->tree->SuspendLayout();
			this->call_put->SuspendLayout();
			this->average->SuspendLayout();
			this->lookback->SuspendLayout();
			this->models->SuspendLayout();
			this->SuspendLayout();
			// 
			// outputBox
			// 
			this->outputBox->BackColor = System::Drawing::SystemColors::WindowFrame;
			this->outputBox->Controls->Add(this->outputString);
			this->outputBox->Font = (gcnew System::Drawing::Font(L"Courier New", 18, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->outputBox->ForeColor = System::Drawing::SystemColors::Control;
			this->outputBox->Location = System::Drawing::Point(22, 499);
			this->outputBox->Name = L"outputBox";
			this->outputBox->Size = System::Drawing::Size(936, 267);
			this->outputBox->TabIndex = 0;
			this->outputBox->TabStop = false;
			this->outputBox->Text = L"Output";
			// 
			// outputString
			// 
			this->outputString->AutoSize = true;
			this->outputString->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->outputString->Location = System::Drawing::Point(23, 31);
			this->outputString->Name = L"outputString";
			this->outputString->Size = System::Drawing::Size(274, 22);
			this->outputString->TabIndex = 0;
			this->outputString->Text = L"Waiting for execution...";
			// 
			// inputBox
			// 
			this->inputBox->Controls->Add(this->MC);
			this->inputBox->Controls->Add(this->tree);
			this->inputBox->Controls->Add(this->call_put);
			this->inputBox->Controls->Add(this->average);
			this->inputBox->Controls->Add(this->lookback);
			this->inputBox->Controls->Add(this->sigma_tb);
			this->inputBox->Controls->Add(this->q_tb);
			this->inputBox->Controls->Add(this->r_tb);
			this->inputBox->Controls->Add(this->T_tb);
			this->inputBox->Controls->Add(this->K_tb);
			this->inputBox->Controls->Add(this->St_tb);
			this->inputBox->Controls->Add(this->label6);
			this->inputBox->Controls->Add(this->label5);
			this->inputBox->Controls->Add(this->label4);
			this->inputBox->Controls->Add(this->label3);
			this->inputBox->Controls->Add(this->label2);
			this->inputBox->Controls->Add(this->label1);
			this->inputBox->Font = (gcnew System::Drawing::Font(L"Courier New", 18, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->inputBox->Location = System::Drawing::Point(22, 120);
			this->inputBox->Name = L"inputBox";
			this->inputBox->Size = System::Drawing::Size(932, 326);
			this->inputBox->TabIndex = 1;
			this->inputBox->TabStop = false;
			this->inputBox->Text = L"Inputs";
			// 
			// MC
			// 
			this->MC->Controls->Add(this->rep_tb);
			this->MC->Controls->Add(this->sims_tb);
			this->MC->Controls->Add(this->label8);
			this->MC->Controls->Add(this->label7);
			this->MC->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->MC->Location = System::Drawing::Point(272, 219);
			this->MC->Name = L"MC";
			this->MC->Size = System::Drawing::Size(306, 90);
			this->MC->TabIndex = 24;
			this->MC->TabStop = false;
			this->MC->Text = L"Monte Carlo";
			// 
			// rep_tb
			// 
			this->rep_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->rep_tb->Location = System::Drawing::Point(213, 55);
			this->rep_tb->Name = L"rep_tb";
			this->rep_tb->Size = System::Drawing::Size(71, 26);
			this->rep_tb->TabIndex = 19;
			// 
			// sims_tb
			// 
			this->sims_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->sims_tb->Location = System::Drawing::Point(213, 23);
			this->sims_tb->Name = L"sims_tb";
			this->sims_tb->Size = System::Drawing::Size(71, 26);
			this->sims_tb->TabIndex = 18;
			// 
			// label8
			// 
			this->label8->AutoSize = true;
			this->label8->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label8->Location = System::Drawing::Point(19, 57);
			this->label8->Name = L"label8";
			this->label8->Size = System::Drawing::Size(118, 18);
			this->label8->TabIndex = 11;
			this->label8->Text = L"Repetitions";
			// 
			// label7
			// 
			this->label7->AutoSize = true;
			this->label7->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label7->Location = System::Drawing::Point(19, 27);
			this->label7->Name = L"label7";
			this->label7->Size = System::Drawing::Size(118, 18);
			this->label7->TabIndex = 10;
			this->label7->Text = L"Simulations";
			// 
			// tree
			// 
			this->tree->Controls->Add(this->layers_tb);
			this->tree->Controls->Add(this->label12);
			this->tree->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->tree->Location = System::Drawing::Point(6, 240);
			this->tree->Name = L"tree";
			this->tree->Size = System::Drawing::Size(240, 69);
			this->tree->TabIndex = 21;
			this->tree->TabStop = false;
			this->tree->Text = L"Tree";
			// 
			// layers_tb
			// 
			this->layers_tb->Location = System::Drawing::Point(142, 28);
			this->layers_tb->Name = L"layers_tb";
			this->layers_tb->Size = System::Drawing::Size(71, 29);
			this->layers_tb->TabIndex = 27;
			// 
			// label12
			// 
			this->label12->AutoSize = true;
			this->label12->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label12->Location = System::Drawing::Point(10, 34);
			this->label12->Name = L"label12";
			this->label12->Size = System::Drawing::Size(118, 18);
			this->label12->TabIndex = 27;
			this->label12->Text = L"Tree layers";
			// 
			// call_put
			// 
			this->call_put->Controls->Add(this->put);
			this->call_put->Controls->Add(this->call);
			this->call_put->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->call_put->Location = System::Drawing::Point(605, 207);
			this->call_put->Name = L"call_put";
			this->call_put->Size = System::Drawing::Size(321, 102);
			this->call_put->TabIndex = 23;
			this->call_put->TabStop = false;
			this->call_put->Text = L"Call / Put";
			// 
			// put
			// 
			this->put->AutoSize = true;
			this->put->Font = (gcnew System::Drawing::Font(L"Courier New", 15.75F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->put->Location = System::Drawing::Point(195, 43);
			this->put->Name = L"put";
			this->put->Size = System::Drawing::Size(67, 27);
			this->put->TabIndex = 1;
			this->put->Text = L"Put";
			this->put->UseVisualStyleBackColor = true;
			// 
			// call
			// 
			this->call->AutoSize = true;
			this->call->Font = (gcnew System::Drawing::Font(L"Courier New", 15.75F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->call->Location = System::Drawing::Point(59, 43);
			this->call->Name = L"call";
			this->call->Size = System::Drawing::Size(80, 27);
			this->call->TabIndex = 0;
			this->call->Text = L"Call";
			this->call->UseVisualStyleBackColor = true;
			// 
			// average
			// 
			this->average->Controls->Add(this->time_elapsed_tb);
			this->average->Controls->Add(this->n_avg_prev_tb);
			this->average->Controls->Add(this->n_avg_tb);
			this->average->Controls->Add(this->StAve_tb);
			this->average->Controls->Add(this->label16);
			this->average->Controls->Add(this->label15);
			this->average->Controls->Add(this->label14);
			this->average->Controls->Add(this->label13);
			this->average->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->average->Location = System::Drawing::Point(602, 29);
			this->average->Name = L"average";
			this->average->Size = System::Drawing::Size(324, 172);
			this->average->TabIndex = 22;
			this->average->TabStop = false;
			this->average->Text = L"Average Option";
			// 
			// time_elapsed_tb
			// 
			this->time_elapsed_tb->Location = System::Drawing::Point(229, 130);
			this->time_elapsed_tb->Name = L"time_elapsed_tb";
			this->time_elapsed_tb->Size = System::Drawing::Size(71, 29);
			this->time_elapsed_tb->TabIndex = 33;
			// 
			// n_avg_prev_tb
			// 
			this->n_avg_prev_tb->Location = System::Drawing::Point(229, 95);
			this->n_avg_prev_tb->Name = L"n_avg_prev_tb";
			this->n_avg_prev_tb->Size = System::Drawing::Size(71, 29);
			this->n_avg_prev_tb->TabIndex = 32;
			// 
			// n_avg_tb
			// 
			this->n_avg_tb->Location = System::Drawing::Point(229, 60);
			this->n_avg_tb->Name = L"n_avg_tb";
			this->n_avg_tb->Size = System::Drawing::Size(71, 29);
			this->n_avg_tb->TabIndex = 31;
			// 
			// StAve_tb
			// 
			this->StAve_tb->Location = System::Drawing::Point(229, 25);
			this->StAve_tb->Name = L"StAve_tb";
			this->StAve_tb->Size = System::Drawing::Size(71, 29);
			this->StAve_tb->TabIndex = 30;
			// 
			// label16
			// 
			this->label16->AutoSize = true;
			this->label16->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label16->Location = System::Drawing::Point(16, 135);
			this->label16->Name = L"label16";
			this->label16->Size = System::Drawing::Size(128, 18);
			this->label16->TabIndex = 30;
			this->label16->Text = L"Time elapsed";
			// 
			// label15
			// 
			this->label15->AutoSize = true;
			this->label15->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label15->Location = System::Drawing::Point(16, 100);
			this->label15->Name = L"label15";
			this->label15->Size = System::Drawing::Size(188, 18);
			this->label15->TabIndex = 29;
			this->label15->Text = L"Prev. trading days";
			// 
			// label14
			// 
			this->label14->AutoSize = true;
			this->label14->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label14->Location = System::Drawing::Point(16, 65);
			this->label14->Name = L"label14";
			this->label14->Size = System::Drawing::Size(128, 18);
			this->label14->TabIndex = 28;
			this->label14->Text = L"Trading days";
			// 
			// label13
			// 
			this->label13->AutoSize = true;
			this->label13->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label13->Location = System::Drawing::Point(16, 30);
			this->label13->Name = L"label13";
			this->label13->Size = System::Drawing::Size(68, 18);
			this->label13->TabIndex = 27;
			this->label13->Text = L"Save,t";
			// 
			// lookback
			// 
			this->lookback->Controls->Add(this->label17);
			this->lookback->Controls->Add(this->n_lookback_tb);
			this->lookback->Controls->Add(this->label11);
			this->lookback->Controls->Add(this->StMax_tb);
			this->lookback->Controls->Add(this->label10);
			this->lookback->Controls->Add(this->StMin_tb);
			this->lookback->Controls->Add(this->label9);
			this->lookback->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->lookback->Location = System::Drawing::Point(272, 29);
			this->lookback->Name = L"lookback";
			this->lookback->Size = System::Drawing::Size(306, 184);
			this->lookback->TabIndex = 20;
			this->lookback->TabStop = false;
			this->lookback->Text = L"Lookback Option";
			// 
			// label17
			// 
			this->label17->AutoSize = true;
			this->label17->Font = (gcnew System::Drawing::Font(L"Courier New", 9.75F, System::Drawing::FontStyle::Italic, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label17->Location = System::Drawing::Point(64, 130);
			this->label17->Name = L"label17";
			this->label17->Size = System::Drawing::Size(176, 34);
			this->label17->TabIndex = 27;
			this->label17->Text = L"(Lookback Option \r\nwith floating strike)";
			// 
			// n_lookback_tb
			// 
			this->n_lookback_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->n_lookback_tb->Location = System::Drawing::Point(213, 92);
			this->n_lookback_tb->Name = L"n_lookback_tb";
			this->n_lookback_tb->Size = System::Drawing::Size(71, 26);
			this->n_lookback_tb->TabIndex = 26;
			// 
			// label11
			// 
			this->label11->AutoSize = true;
			this->label11->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label11->Location = System::Drawing::Point(19, 94);
			this->label11->Name = L"label11";
			this->label11->Size = System::Drawing::Size(128, 18);
			this->label11->TabIndex = 21;
			this->label11->Text = L"Trading days";
			// 
			// StMax_tb
			// 
			this->StMax_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->StMax_tb->Location = System::Drawing::Point(213, 60);
			this->StMax_tb->Name = L"StMax_tb";
			this->StMax_tb->Size = System::Drawing::Size(71, 26);
			this->StMax_tb->TabIndex = 25;
			// 
			// label10
			// 
			this->label10->AutoSize = true;
			this->label10->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label10->Location = System::Drawing::Point(19, 62);
			this->label10->Name = L"label10";
			this->label10->Size = System::Drawing::Size(168, 18);
			this->label10->TabIndex = 22;
			this->label10->Text = L"Smax,t (for Put)";
			// 
			// StMin_tb
			// 
			this->StMin_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->StMin_tb->Location = System::Drawing::Point(213, 28);
			this->StMin_tb->Name = L"StMin_tb";
			this->StMin_tb->Size = System::Drawing::Size(71, 26);
			this->StMin_tb->TabIndex = 24;
			// 
			// label9
			// 
			this->label9->AutoSize = true;
			this->label9->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label9->Location = System::Drawing::Point(19, 30);
			this->label9->Name = L"label9";
			this->label9->Size = System::Drawing::Size(178, 18);
			this->label9->TabIndex = 23;
			this->label9->Text = L"Smin,t (for Call)";
			// 
			// sigma_tb
			// 
			this->sigma_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->sigma_tb->Location = System::Drawing::Point(148, 188);
			this->sigma_tb->Name = L"sigma_tb";
			this->sigma_tb->Size = System::Drawing::Size(71, 26);
			this->sigma_tb->TabIndex = 17;
			// 
			// q_tb
			// 
			this->q_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->q_tb->Location = System::Drawing::Point(148, 156);
			this->q_tb->Name = L"q_tb";
			this->q_tb->Size = System::Drawing::Size(71, 26);
			this->q_tb->TabIndex = 16;
			// 
			// r_tb
			// 
			this->r_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->r_tb->Location = System::Drawing::Point(148, 124);
			this->r_tb->Name = L"r_tb";
			this->r_tb->Size = System::Drawing::Size(71, 26);
			this->r_tb->TabIndex = 15;
			// 
			// T_tb
			// 
			this->T_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->T_tb->Location = System::Drawing::Point(148, 93);
			this->T_tb->Name = L"T_tb";
			this->T_tb->Size = System::Drawing::Size(71, 26);
			this->T_tb->TabIndex = 14;
			// 
			// K_tb
			// 
			this->K_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->K_tb->Location = System::Drawing::Point(148, 61);
			this->K_tb->Name = L"K_tb";
			this->K_tb->Size = System::Drawing::Size(71, 26);
			this->K_tb->TabIndex = 13;
			// 
			// St_tb
			// 
			this->St_tb->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->St_tb->Location = System::Drawing::Point(148, 29);
			this->St_tb->Name = L"St_tb";
			this->St_tb->Size = System::Drawing::Size(71, 26);
			this->St_tb->TabIndex = 12;
			// 
			// label6
			// 
			this->label6->AutoSize = true;
			this->label6->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label6->Location = System::Drawing::Point(16, 190);
			this->label6->Name = L"label6";
			this->label6->Size = System::Drawing::Size(58, 18);
			this->label6->TabIndex = 9;
			this->label6->Text = L"sigma";
			// 
			// label5
			// 
			this->label5->AutoSize = true;
			this->label5->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label5->Location = System::Drawing::Point(16, 158);
			this->label5->Name = L"label5";
			this->label5->Size = System::Drawing::Size(18, 18);
			this->label5->TabIndex = 8;
			this->label5->Text = L"q";
			// 
			// label4
			// 
			this->label4->AutoSize = true;
			this->label4->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label4->Location = System::Drawing::Point(16, 126);
			this->label4->Name = L"label4";
			this->label4->Size = System::Drawing::Size(18, 18);
			this->label4->TabIndex = 7;
			this->label4->Text = L"r";
			// 
			// label3
			// 
			this->label3->AutoSize = true;
			this->label3->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label3->Location = System::Drawing::Point(16, 95);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(18, 18);
			this->label3->TabIndex = 6;
			this->label3->Text = L"T";
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label2->Location = System::Drawing::Point(16, 63);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(18, 18);
			this->label2->TabIndex = 5;
			this->label2->Text = L"K";
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label1->Location = System::Drawing::Point(16, 31);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(108, 18);
			this->label1->TabIndex = 4;
			this->label1->Text = L"Spot Price";
			// 
			// calc
			// 
			this->calc->Font = (gcnew System::Drawing::Font(L"Courier New", 15.75F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->calc->Location = System::Drawing::Point(686, 452);
			this->calc->Name = L"calc";
			this->calc->Size = System::Drawing::Size(272, 41);
			this->calc->TabIndex = 4;
			this->calc->Text = L"Calculate !";
			this->calc->UseVisualStyleBackColor = true;
			this->calc->Click += gcnew System::EventHandler(this, &mainForm::calc_Click);
			// 
			// author
			// 
			this->author->AutoSize = true;
			this->author->Font = (gcnew System::Drawing::Font(L"Calibri", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->author->Location = System::Drawing::Point(21, 775);
			this->author->Name = L"author";
			this->author->Size = System::Drawing::Size(537, 19);
			this->author->TabIndex = 5;
			this->author->Text = L"Coded by Alex Chen ( 陳柏言 ), Nationl Taiwan University, Department of Finance";
			// 
			// email
			// 
			this->email->AutoSize = true;
			this->email->Font = (gcnew System::Drawing::Font(L"Calibri", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->email->Location = System::Drawing::Point(21, 804);
			this->email->Name = L"email";
			this->email->Size = System::Drawing::Size(247, 19);
			this->email->TabIndex = 6;
			this->email->Text = L"Contact me : r10723046@ntu.edu.tw";
			// 
			// models
			// 
			this->models->Controls->Add(this->EU_avg_MC);
			this->models->Controls->Add(this->EU_lb_MC);
			this->models->Controls->Add(this->US_CRR);
			this->models->Controls->Add(this->EU_CRR);
			this->models->Controls->Add(this->EU_MC);
			this->models->Font = (gcnew System::Drawing::Font(L"Courier New", 18, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->models->Location = System::Drawing::Point(25, 19);
			this->models->Name = L"models";
			this->models->Size = System::Drawing::Size(929, 95);
			this->models->TabIndex = 7;
			this->models->TabStop = false;
			this->models->Text = L"Pricing Models";
			// 
			// EU_avg_MC
			// 
			this->EU_avg_MC->AutoSize = true;
			this->EU_avg_MC->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EU_avg_MC->Location = System::Drawing::Point(327, 63);
			this->EU_avg_MC->Name = L"EU_avg_MC";
			this->EU_avg_MC->Size = System::Drawing::Size(237, 26);
			this->EU_avg_MC->TabIndex = 4;
			this->EU_avg_MC->TabStop = true;
			this->EU_avg_MC->Text = L"European average MC";
			this->EU_avg_MC->UseVisualStyleBackColor = true;
			// 
			// EU_lb_MC
			// 
			this->EU_lb_MC->AutoSize = true;
			this->EU_lb_MC->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EU_lb_MC->Location = System::Drawing::Point(327, 31);
			this->EU_lb_MC->Name = L"EU_lb_MC";
			this->EU_lb_MC->Size = System::Drawing::Size(248, 26);
			this->EU_lb_MC->TabIndex = 3;
			this->EU_lb_MC->TabStop = true;
			this->EU_lb_MC->Text = L"European lookback MC";
			this->EU_lb_MC->UseVisualStyleBackColor = true;
			// 
			// US_CRR
			// 
			this->US_CRR->AutoSize = true;
			this->US_CRR->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->US_CRR->Location = System::Drawing::Point(653, 63);
			this->US_CRR->Name = L"US_CRR";
			this->US_CRR->Size = System::Drawing::Size(160, 26);
			this->US_CRR->TabIndex = 2;
			this->US_CRR->TabStop = true;
			this->US_CRR->Text = L"American CRR";
			this->US_CRR->UseVisualStyleBackColor = true;
			// 
			// EU_CRR
			// 
			this->EU_CRR->AutoSize = true;
			this->EU_CRR->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EU_CRR->Location = System::Drawing::Point(653, 31);
			this->EU_CRR->Name = L"EU_CRR";
			this->EU_CRR->Size = System::Drawing::Size(160, 26);
			this->EU_CRR->TabIndex = 1;
			this->EU_CRR->TabStop = true;
			this->EU_CRR->Text = L"European CRR";
			this->EU_CRR->UseVisualStyleBackColor = true;
			// 
			// EU_MC
			// 
			this->EU_MC->AutoSize = true;
			this->EU_MC->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EU_MC->Location = System::Drawing::Point(94, 31);
			this->EU_MC->Name = L"EU_MC";
			this->EU_MC->Size = System::Drawing::Size(149, 26);
			this->EU_MC->TabIndex = 0;
			this->EU_MC->TabStop = true;
			this->EU_MC->Text = L"European MC";
			this->EU_MC->UseVisualStyleBackColor = true;
			// 
			// mainForm
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 12);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::Menu;
			this->ClientSize = System::Drawing::Size(984, 836);
			this->Controls->Add(this->models);
			this->Controls->Add(this->email);
			this->Controls->Add(this->author);
			this->Controls->Add(this->calc);
			this->Controls->Add(this->inputBox);
			this->Controls->Add(this->outputBox);
			this->MaximumSize = System::Drawing::Size(1000, 875);
			this->MinimumSize = System::Drawing::Size(1000, 875);
			this->Name = L"mainForm";
			this->Text = L"Option Price Calculator";
			this->outputBox->ResumeLayout(false);
			this->outputBox->PerformLayout();
			this->inputBox->ResumeLayout(false);
			this->inputBox->PerformLayout();
			this->MC->ResumeLayout(false);
			this->MC->PerformLayout();
			this->tree->ResumeLayout(false);
			this->tree->PerformLayout();
			this->call_put->ResumeLayout(false);
			this->call_put->PerformLayout();
			this->average->ResumeLayout(false);
			this->average->PerformLayout();
			this->lookback->ResumeLayout(false);
			this->lookback->PerformLayout();
			this->models->ResumeLayout(false);
			this->models->PerformLayout();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void calc_Click(System::Object^ sender, System::EventArgs^ e) {
		// American Option(CRR)
		// European Option(CRR)
		// European Option(MC)
		// Lookback European Option(MC)
		// Average European Option(MC)

		this->outputString->Text = "Wrong input. Please restart application......";

		// General
		String^ St_string = St_tb->Text;
		String^ T_string = T_tb->Text;
		String^ r_string = r_tb->Text;
		String^ q_string = q_tb->Text;
		String^ sigma_string = sigma_tb->Text;

		double St = System::Convert::ToDouble(St_string);
		double T = System::Convert::ToDouble(T_string);
		double r = System::Convert::ToDouble(r_string);
		double q = System::Convert::ToDouble(q_string);
		double sigma = System::Convert::ToDouble(sigma_string);


		// Vanila MC
		if (EU_MC->Checked == true) {
			String^ K_string = K_tb->Text;
			String^ sims_string = sims_tb->Text;
			String^ rep_string = rep_tb->Text;

			double K = System::Convert::ToDouble(K_string);
			int sims = System::Convert::ToInt64(sims_string);
			int rep = System::Convert::ToInt64(rep_string);

			// start calulating...
			vector<double> meanLst;
			int times = 0;

			default_random_engine generator;
			generator.seed(chrono::system_clock::now().time_since_epoch().count());
			normal_distribution<double> distribution(log(St) + (r - q - 0.5 * (pow(sigma, 2))) * T, sigma * sqrt(T));

			while (times < rep) {
				vector<double> stockSamples;
				for (int i = 0; i < sims; i++) {
					double lnSample = distribution(generator);
					// cout << lnSample << endl;
					double sample = exp(lnSample);
					// cout << sample << endl;
					stockSamples.push_back(sample);
				}

				vector<double> optionValue;
				if (call->Checked == true) {
					for (int j = 0; j < sims; j++) {
						optionValue.push_back(max(stockSamples[j] - K, 0.0));
					}
					double sum = 0;
					for (int k = 0; k < sims; k++) {
						sum += optionValue[k];
					}
					double mean = sum / sims;
					double discounted = mean * exp(-r * T);
					meanLst.push_back(discounted);
					times += 1;
				}
				else if (put->Checked == true) {
					for (int l = 0; l < sims; l++) {
						optionValue.push_back(max(K - stockSamples[l], 0.0));
					}
					double sum = 0;
					for (int k = 0; k < sims; k++) {
						sum += optionValue[k];
					}
					double mean = sum / sims;
					double discounted = mean * exp(-r * T);
					meanLst.push_back(discounted);
					times += 1;
				}
			}

			double sum_mean = 0;
			for (int i = 0; i < rep; i++) {
				sum_mean += meanLst[i];
			}
			double meanOfRep = sum_mean / rep;

			double var = 0.0;
			for (int n = 0; n < rep; n++) {
				var += (meanLst[n] - meanOfRep) * (meanLst[n] - meanOfRep);
			}
			var = var / rep;
			double sdOfRep = sqrt(var);
			double upper = meanOfRep + 2 * sdOfRep;
			double lower = meanOfRep - 2 * sdOfRep;

			//round
			meanOfRep = round(meanOfRep * 1000.0) / 1000.0;
			sdOfRep = round(sdOfRep * 1000.0) / 1000.0;
			upper = round(upper * 1000.0) / 1000.0;
			lower = round(lower * 1000.0) / 1000.0;

			if (call->Checked == true) {
				this->outputString->Text = "================================================================================\nEuropean Call\n--------------------------------------------------------------------------------\nmean : " 
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}
			else if (put->Checked == true) {
				this->outputString->Text = "================================================================================\nEuropean Put\n--------------------------------------------------------------------------------\nmean : "
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}
		}



		// Lookback MC
		else if (EU_lb_MC->Checked == true) {
			String^ n_lb_string = n_lookback_tb->Text;
			String^ sims_string = sims_tb->Text;
			String^ rep_string = rep_tb->Text;

			int n_lb = System::Convert::ToInt64(n_lb_string);
			int sims = System::Convert::ToInt64(sims_string);
			int rep = System::Convert::ToInt64(rep_string);

			if (call->Checked == true) {
				String^ StMin_string = StMin_tb->Text;
				double StMin = System::Convert::ToDouble(StMin_string);

				double dt = T / n_lb;
				int times = 0;

				default_random_engine generator;
				generator.seed(chrono::system_clock::now().time_since_epoch().count());
				normal_distribution<double> distribution((r - q - 0.5 * (pow(sigma, 2)))* dt, sigma* sqrt(dt));

				vector<double> means;
				while (times < rep) {
					vector<double> optionValue;

					for (int i = 0; i < sims; i++) {
						double minPrice = StMin;
						vector<double> stockPrices;
						stockPrices.push_back(log(St));

						for (int j = 1; j < n_lb + 1; j++) {
							double dlnS = distribution(generator);
							double sample = stockPrices[j - 1] + dlnS;
							stockPrices.push_back(sample);
						}
						for (int k = 0; k < n_lb + 1; k++) {
							stockPrices[k] = exp(stockPrices[k]);
							if (stockPrices[k] < minPrice) {
								minPrice = stockPrices[k];
							}
						}
						// for each loop, single price path is simulated...
						double callValue = max(stockPrices[n_lb] - minPrice, 0.0) * exp(-r * T);
						optionValue.push_back(callValue);
					}

					double sum = 0;
					for (int i = 0; i < sims; i++) {
						sum += optionValue[i];
					}
					double mean = sum / sims;
					means.push_back(mean);
					times += 1;
				}

				double sum_means = 0;
				for (int l = 0; l < rep; l++) {
					sum_means += means[l];
				}
				double meanOfRep = sum_means / rep;

				double var = 0.0;
				for (int n = 0; n < rep; n++) {
					var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
				}
				var = var / rep;
				double sdOfRep = sqrt(var);
				double upper = meanOfRep + 2 * sdOfRep;
				double lower = meanOfRep - 2 * sdOfRep;

				//round
				meanOfRep = round(meanOfRep * 1000.0) / 1000.0;
				sdOfRep = round(sdOfRep * 1000.0) / 1000.0;
				upper = round(upper * 1000.0) / 1000.0;
				lower = round(lower * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Lookback Call\n--------------------------------------------------------------------------------\nmean : "
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}

			else if (put->Checked == true) {
				String^ StMax_string = StMax_tb->Text;
				double StMax = System::Convert::ToDouble(StMax_string);

				double dt = T / n_lb;
				int times = 0;

				default_random_engine generator;
				generator.seed(chrono::system_clock::now().time_since_epoch().count());
				normal_distribution<double> distribution((r - q - 0.5 * (pow(sigma, 2)))* dt, sigma* sqrt(dt));

				vector<double> means;
				while (times < rep) {
					vector<double> optionValue;

					for (int i = 0; i < sims; i++) {
						double maxPrice = StMax;
						vector<double> stockPrices;
						stockPrices.push_back(log(St));

						for (int j = 1; j < n_lb + 1; j++) {
							double dlnS = distribution(generator);
							double sample = stockPrices[j - 1] + dlnS;
							stockPrices.push_back(sample);
						}
						for (int k = 0; k < n_lb + 1; k++) {
							stockPrices[k] = exp(stockPrices[k]);
							if (stockPrices[k] > maxPrice) {
								maxPrice = stockPrices[k];
							}
						}
						// for each loop, single price path is simulated...
						double putValue = max(maxPrice - stockPrices[n_lb], 0.0) * exp(-r * T);
						optionValue.push_back(putValue);
					}

					double sum = 0;
					for (int i = 0; i < sims; i++) {
						sum += optionValue[i];
					}
					double mean = sum / sims;
					means.push_back(mean);
					times += 1;
				}

				double sum_means = 0;
				for (int l = 0; l < rep; l++) {
					sum_means += means[l];
				}
				double meanOfRep = sum_means / rep;

				double var = 0.0;
				for (int n = 0; n < rep; n++) {
					var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
				}
				var = var / rep;
				double sdOfRep = sqrt(var);
				double upper = meanOfRep + 2 * sdOfRep;
				double lower = meanOfRep - 2 * sdOfRep;

				//round
				meanOfRep = round(meanOfRep * 1000.0) / 1000.0;
				sdOfRep = round(sdOfRep * 1000.0) / 1000.0;
				upper = round(upper * 1000.0) / 1000.0;
				lower = round(lower * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Lookback Put\n--------------------------------------------------------------------------------\nmean : "
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}
		}



		// Average MC
		else if (EU_avg_MC->Checked == true) {
			String^ K_string = K_tb->Text;
			String^ StAve_string = StAve_tb->Text;
			String^ n_avg_string = n_avg_tb->Text;
			String^ n_avg_prev_string = n_avg_prev_tb->Text;
			String^ time_elapsed_string = time_elapsed_tb->Text;
			String^ sims_string = sims_tb->Text;
			String^ rep_string = rep_tb->Text;

			double K = System::Convert::ToDouble(K_string);
			double StAve = System::Convert::ToDouble(StAve_string);
			int n_avg = System::Convert::ToInt64(n_avg_string);
			int n_avg_prev = System::Convert::ToInt64(n_avg_prev_string);
			double time_elapsed = System::Convert::ToDouble(time_elapsed_string);
			int sims = System::Convert::ToInt64(sims_string);
			int rep = System::Convert::ToInt64(rep_string);

			if (call->Checked == true) {
				double dt = T / n_avg;
				int times = 0;

				default_random_engine generator;
				generator.seed(chrono::system_clock::now().time_since_epoch().count());
				normal_distribution<double> distribution((r - q - 0.5 * (pow(sigma, 2)))* dt, sigma* sqrt(dt));

				vector<double> means;
				while (times < rep) {
					vector<double> optionValue;

					for (int i = 0; i < sims; i++) {
						vector<double> stockPrices;
						stockPrices.push_back(log(St));

						for (int j = 1; j < n_avg + 1; j++) {
							double dlnS = distribution(generator);
							double sample = stockPrices[j - 1] + dlnS;
							stockPrices.push_back(sample);
						}
						for (int k = 0; k < n_avg + 1; k++) {
							stockPrices[k] = exp(stockPrices[k]);
						}
						// for each loop, single price path is simulated...

						double callValue;
						if (time_elapsed == 0) {
							double sum_stockPrice = 0;
							for (int l = 0; l < n_avg + 1; l++) {
								sum_stockPrice += stockPrices[l];
							}
							double mean_stockPrice = sum_stockPrice / (n_avg + 1);
							callValue = max(mean_stockPrice - K, 0.0) * exp(-r * T);
							optionValue.push_back(callValue);
						}
						else {
							double sum_stockPrice = 0;
							for (int l = 1; l < n_avg + 1; l++) {
								sum_stockPrice += stockPrices[l];
							}
							double payoff = (StAve * (n_avg_prev + 1) + sum_stockPrice) / (n_avg_prev + n_avg + 1) - K;
							callValue = max(payoff, 0.0) * exp(-r * T);
							optionValue.push_back(callValue);
						}
					}
					double sum = 0;
					for (int i = 0; i < sims; i++) {
						sum += optionValue[i];
					}
					double mean = sum / sims;
					means.push_back(mean);
					times += 1;
				}

				double sum_means = 0;
				for (int l = 0; l < rep; l++) {
					sum_means += means[l];
				}
				double meanOfRep = sum_means / rep;

				double var = 0.0;
				for (int n = 0; n < rep; n++) {
					var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
				}
				var = var / rep;
				double sdOfRep = sqrt(var);
				double upper = meanOfRep + 2 * sdOfRep;
				double lower = meanOfRep - 2 * sdOfRep;

				//round
				meanOfRep = round(meanOfRep * 1000.0) / 1000.0;
				sdOfRep = round(sdOfRep * 1000.0) / 1000.0;
				upper = round(upper * 1000.0) / 1000.0;
				lower = round(lower * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Average Call\n--------------------------------------------------------------------------------\nmean : "
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}
			else if (put->Checked == true) {
				double dt = T / n_avg;
				int times = 0;

				default_random_engine generator;
				generator.seed(chrono::system_clock::now().time_since_epoch().count());
				normal_distribution<double> distribution((r - q - 0.5 * (pow(sigma, 2)))* dt, sigma* sqrt(dt));

				vector<double> means;
				while (times < rep) {
					vector<double> optionValue;

					for (int i = 0; i < sims; i++) {
						vector<double> stockPrices;
						stockPrices.push_back(log(St));

						for (int j = 1; j < n_avg + 1; j++) {
							double dlnS = distribution(generator);
							double sample = stockPrices[j - 1] + dlnS;
							stockPrices.push_back(sample);
						}
						for (int k = 0; k < n_avg + 1; k++) {
							stockPrices[k] = exp(stockPrices[k]);
						}
						// for each loop, single price path is simulated...

						double putValue;
						if (time_elapsed == 0) {
							double sum_stockPrice = 0;
							for (int l = 0; l < n_avg + 1; l++) {
								sum_stockPrice += stockPrices[l];
							}
							double mean_stockPrice = sum_stockPrice / (n_avg + 1);
							putValue = max(K - mean_stockPrice, 0.0) * exp(-r * T);
							optionValue.push_back(putValue);
						}
						else {
							double sum_stockPrice = 0;
							for (int l = 1; l < n_avg + 1; l++) {
								sum_stockPrice += stockPrices[l];
							}
							double payoff = K - (StAve * (n_avg_prev + 1) + sum_stockPrice) / (n_avg_prev + n_avg + 1);
							putValue = max(payoff, 0.0) * exp(-r * T);
							optionValue.push_back(putValue);
						}
					}
					double sum = 0;
					for (int i = 0; i < sims; i++) {
						sum += optionValue[i];
					}
					double mean = sum / sims;
					means.push_back(mean);
					times += 1;
				}

				double sum_means = 0;
				for (int l = 0; l < rep; l++) {
					sum_means += means[l];
				}
				double meanOfRep = sum_means / rep;

				double var = 0.0;
				for (int n = 0; n < rep; n++) {
					var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
				}
				var = var / rep;
				double sdOfRep = sqrt(var);
				double upper = meanOfRep + 2 * sdOfRep;
				double lower = meanOfRep - 2 * sdOfRep;

				//round
				meanOfRep = round(meanOfRep * 1000.0) / 1000.0;
				sdOfRep = round(sdOfRep * 1000.0) / 1000.0;
				upper = round(upper * 1000.0) / 1000.0;
				lower = round(lower * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Average Put\n--------------------------------------------------------------------------------\nmean : "
					+ meanOfRep + "\n" + "standard error : " + sdOfRep + "\n" + "0.95 confidence interval : [ " + lower + ", " + upper + " ]";
			}
		}



		// EU Tree
		else if (EU_CRR->Checked == true) {
			String^ K_string = K_tb->Text;
			String^ layers_string = layers_tb->Text;

			double K = System::Convert::ToDouble(K_string);
			int layers = System::Convert::ToInt64(layers_string);

			// start calculating
			double dt = T / layers;
			double u = exp(sigma * sqrt(dt));
			double d = exp(-sigma * sqrt(dt));
			double p = (exp((r - q) * dt) - d) / (u - d);

			vector<double> stockPrice;
			for (int j = 0; j < layers + 1; j++) {
				stockPrice.push_back((St * pow(u, layers - j) * pow(d, j)));
			}

			if (call->Checked == true) {
				vector<double> callPrice;
				for (int j = 0; j < layers + 1; j++) {
					callPrice.push_back(max(stockPrice[j] - K, 0.0));
				}
				int times = 0;
				int i_temp = layers - 1;
				while (times < layers) {
					for (int j = 0; j < i_temp + 1; j++) {
						callPrice[j] = (callPrice[j] * p + callPrice[j + 1] * (1 - p)) * exp(-r * dt);
					}
					i_temp -= 1;
					times += 1;
				}

				// round
				callPrice[0] = round(callPrice[0] * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Call\n--------------------------------------------------------------------------------\nPrice : "
					+ callPrice[0] + " (CRR Binomial Tree)";
			}
			else if (put->Checked == true) {
				vector<double> putPrice;
				for (int j = 0; j < layers + 1; j++) {
					putPrice.push_back(max(K - stockPrice[j], 0.0));
				}
				int times = 0;
				int i_temp = layers - 1;
				while (times < layers) {
					for (int j = 0; j < i_temp + 1; j++) {
						putPrice[j] = (putPrice[j] * p + putPrice[j + 1] * (1 - p)) * exp(-r * dt);
					}
					i_temp -= 1;
					times += 1;
				}
				// round
				putPrice[0] = round(putPrice[0] * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nEuropean Put\n--------------------------------------------------------------------------------\nPrice : "
					+ putPrice[0] + " (CRR Binomial Tree)";
			}
		}



		// US Tree
		else if (US_CRR->Checked == true) {
			String^ K_string = K_tb->Text;
			String^ layers_string = layers_tb->Text;

			double K = System::Convert::ToDouble(K_string);
			int layers = System::Convert::ToInt64(layers_string);

			if (call->Checked == true) {}
			else if (put->Checked == true) {}

			double dt = T / layers;
			double u = exp(sigma * sqrt(dt));
			double d = exp(-sigma * sqrt(dt));
			double p = (exp((r - q) * dt) - d) / (u - d);

			// simulate stock price
			vector<vector<double>> stockPrice;
			for (int i = 0; i < layers + 1; i++) {
				vector<double> temp;
				for (int j = 0; j < i + 1; j++) {
					temp.push_back(0);
				}
				stockPrice.push_back(temp);
			}
			for (int i = 0; i < layers + 1; i++) {
				for (int j = 0; j < i + 1; j++) {
					stockPrice[i][j] = St * pow(u, i - j) * pow(d, j);
				}
			}

			if (call->Checked == true) {
				// calculate terminal payoff
				vector<double> callPrice;
				for (int j = 0; j < layers + 1; j++) {
					callPrice.push_back(max(stockPrice[layers][j] - K, 0.0));
				}
				int times = 0;
				int i_temp = layers - 1;
				while (times < layers) {
					vector<double> xValue;
					for (int j = 0; j < i_temp + 1; j++) {
						callPrice[j] = (callPrice[j] * p + callPrice[j + 1] * (1 - p)) * exp(-r * dt);
						// calculate excersise value and compare it to holding value...
					}
					for (int k = 0; k < i_temp - 1; k++) {
						xValue.push_back(max(stockPrice[i_temp][k] - K, 0.0));
						callPrice[k] = max(callPrice[k], xValue[k]);
					}
					i_temp -= 1;
					times += 1;
				}
				callPrice[0] = round(callPrice[0] * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nAmerican Call\n--------------------------------------------------------------------------------\nPrice : "
					+ callPrice[0] + " (CRR Binomial Tree)";
			}
			else if (put->Checked == true) {
				vector<double> putPrice;
				for (int j = 0; j < layers + 1; j++) {
					putPrice.push_back((K - stockPrice[layers][j], 0.0));
				}

				int times = 0;
				int i_temp = layers - 1;
				while (times < layers) {
					vector<double> xValue;
					for (int j = 0; j < i_temp + 1; j++) {
						putPrice[j] = (putPrice[j] * p + putPrice[j + 1] * (1 - p)) * exp(-r * dt);
						// calculate excersise value and compare it to holding value...
					}
					for (int k = 0; k < i_temp + 1; k++) {
						xValue.push_back(max(K - stockPrice[i_temp][k], 0.0));
						putPrice[k] = max(putPrice[k], xValue[k]);
					}
					i_temp -= 1;
					times += 1;
				}
				putPrice[0] = round(putPrice[0] * 1000.0) / 1000.0;

				this->outputString->Text = "================================================================================\nAmerican Put\n--------------------------------------------------------------------------------\nPrice : "
					+ putPrice[0] + " (CRR Binomial Tree)";
			}
		}
	}
};
}
