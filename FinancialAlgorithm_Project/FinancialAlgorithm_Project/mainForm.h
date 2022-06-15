#pragma once

namespace FinAlgoProhect {

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
	private: System::Windows::Forms::ListBox^ models;
	private: System::Windows::Forms::Label^ label0;
	private: System::Windows::Forms::Label^ label1;
	private: System::Windows::Forms::Label^ label8;
	private: System::Windows::Forms::Label^ label7;
	private: System::Windows::Forms::Label^ label6;
	private: System::Windows::Forms::Label^ label5;
	private: System::Windows::Forms::Label^ label4;
	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::Label^ label2;
	private: System::Windows::Forms::TextBox^ sims;

	private: System::Windows::Forms::TextBox^ sigma;

	private: System::Windows::Forms::TextBox^ q;

	private: System::Windows::Forms::TextBox^ r;

	private: System::Windows::Forms::TextBox^ T;

	private: System::Windows::Forms::TextBox^ K;
	private: System::Windows::Forms::TextBox^ St;
	private: System::Windows::Forms::TextBox^ rep;
	private: System::Windows::Forms::GroupBox^ lookback;
	private: System::Windows::Forms::TextBox^ n_lookback;

	private: System::Windows::Forms::Label^ label11;
	private: System::Windows::Forms::TextBox^ StMax;

	private: System::Windows::Forms::Label^ label10;
	private: System::Windows::Forms::TextBox^ StMin;

	private: System::Windows::Forms::Label^ label9;
	private: System::Windows::Forms::GroupBox^ tree;

	private: System::Windows::Forms::TextBox^ layers;
	private: System::Windows::Forms::Label^ label12;
	private: System::Windows::Forms::CheckBox^ US;
	private: System::Windows::Forms::CheckBox^ euro;
	private: System::Windows::Forms::GroupBox^ average;
	private: System::Windows::Forms::Label^ label13;
	private: System::Windows::Forms::CheckBox^ put;
	private: System::Windows::Forms::CheckBox^ call;
	private: System::Windows::Forms::TextBox^ time_elapsed;
	private: System::Windows::Forms::TextBox^ n_avg_prev;
	private: System::Windows::Forms::TextBox^ n_avg;
	private: System::Windows::Forms::TextBox^ StAve;
	private: System::Windows::Forms::Label^ label16;
	private: System::Windows::Forms::Label^ label15;
	private: System::Windows::Forms::Label^ label14;
	private: System::Windows::Forms::Button^ calc;
	private: System::Windows::Forms::Label^ outputString;




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
			this->put = (gcnew System::Windows::Forms::CheckBox());
			this->call = (gcnew System::Windows::Forms::CheckBox());
			this->average = (gcnew System::Windows::Forms::GroupBox());
			this->time_elapsed = (gcnew System::Windows::Forms::TextBox());
			this->n_avg_prev = (gcnew System::Windows::Forms::TextBox());
			this->n_avg = (gcnew System::Windows::Forms::TextBox());
			this->StAve = (gcnew System::Windows::Forms::TextBox());
			this->label16 = (gcnew System::Windows::Forms::Label());
			this->label15 = (gcnew System::Windows::Forms::Label());
			this->label14 = (gcnew System::Windows::Forms::Label());
			this->label13 = (gcnew System::Windows::Forms::Label());
			this->tree = (gcnew System::Windows::Forms::GroupBox());
			this->US = (gcnew System::Windows::Forms::CheckBox());
			this->euro = (gcnew System::Windows::Forms::CheckBox());
			this->layers = (gcnew System::Windows::Forms::TextBox());
			this->label12 = (gcnew System::Windows::Forms::Label());
			this->lookback = (gcnew System::Windows::Forms::GroupBox());
			this->n_lookback = (gcnew System::Windows::Forms::TextBox());
			this->label11 = (gcnew System::Windows::Forms::Label());
			this->StMax = (gcnew System::Windows::Forms::TextBox());
			this->label10 = (gcnew System::Windows::Forms::Label());
			this->StMin = (gcnew System::Windows::Forms::TextBox());
			this->label9 = (gcnew System::Windows::Forms::Label());
			this->rep = (gcnew System::Windows::Forms::TextBox());
			this->sims = (gcnew System::Windows::Forms::TextBox());
			this->sigma = (gcnew System::Windows::Forms::TextBox());
			this->q = (gcnew System::Windows::Forms::TextBox());
			this->r = (gcnew System::Windows::Forms::TextBox());
			this->T = (gcnew System::Windows::Forms::TextBox());
			this->K = (gcnew System::Windows::Forms::TextBox());
			this->St = (gcnew System::Windows::Forms::TextBox());
			this->label8 = (gcnew System::Windows::Forms::Label());
			this->label7 = (gcnew System::Windows::Forms::Label());
			this->label6 = (gcnew System::Windows::Forms::Label());
			this->label5 = (gcnew System::Windows::Forms::Label());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->models = (gcnew System::Windows::Forms::ListBox());
			this->label0 = (gcnew System::Windows::Forms::Label());
			this->calc = (gcnew System::Windows::Forms::Button());
			this->outputBox->SuspendLayout();
			this->inputBox->SuspendLayout();
			this->average->SuspendLayout();
			this->tree->SuspendLayout();
			this->lookback->SuspendLayout();
			this->SuspendLayout();
			// 
			// outputBox
			// 
			this->outputBox->BackColor = System::Drawing::SystemColors::WindowFrame;
			this->outputBox->Controls->Add(this->outputString);
			this->outputBox->Font = (gcnew System::Drawing::Font(L"Courier New", 18, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->outputBox->ForeColor = System::Drawing::SystemColors::Control;
			this->outputBox->Location = System::Drawing::Point(23, 418);
			this->outputBox->Name = L"outputBox";
			this->outputBox->Size = System::Drawing::Size(936, 321);
			this->outputBox->TabIndex = 0;
			this->outputBox->TabStop = false;
			this->outputBox->Text = L"Output";
			// 
			// outputString
			// 
			this->outputString->AutoSize = true;
			this->outputString->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->outputString->Location = System::Drawing::Point(15, 31);
			this->outputString->Name = L"outputString";
			this->outputString->Size = System::Drawing::Size(248, 18);
			this->outputString->TabIndex = 0;
			this->outputString->Text = L"Waiting for execution...";
			// 
			// inputBox
			// 
			this->inputBox->Controls->Add(this->put);
			this->inputBox->Controls->Add(this->call);
			this->inputBox->Controls->Add(this->average);
			this->inputBox->Controls->Add(this->tree);
			this->inputBox->Controls->Add(this->lookback);
			this->inputBox->Controls->Add(this->rep);
			this->inputBox->Controls->Add(this->sims);
			this->inputBox->Controls->Add(this->sigma);
			this->inputBox->Controls->Add(this->q);
			this->inputBox->Controls->Add(this->r);
			this->inputBox->Controls->Add(this->T);
			this->inputBox->Controls->Add(this->K);
			this->inputBox->Controls->Add(this->St);
			this->inputBox->Controls->Add(this->label8);
			this->inputBox->Controls->Add(this->label7);
			this->inputBox->Controls->Add(this->label6);
			this->inputBox->Controls->Add(this->label5);
			this->inputBox->Controls->Add(this->label4);
			this->inputBox->Controls->Add(this->label3);
			this->inputBox->Controls->Add(this->label2);
			this->inputBox->Controls->Add(this->label1);
			this->inputBox->Font = (gcnew System::Drawing::Font(L"Courier New", 18, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->inputBox->Location = System::Drawing::Point(23, 63);
			this->inputBox->Name = L"inputBox";
			this->inputBox->Size = System::Drawing::Size(932, 302);
			this->inputBox->TabIndex = 1;
			this->inputBox->TabStop = false;
			this->inputBox->Text = L"Inputs";
			// 
			// put
			// 
			this->put->AutoSize = true;
			this->put->Location = System::Drawing::Point(674, 251);
			this->put->Name = L"put";
			this->put->Size = System::Drawing::Size(171, 31);
			this->put->TabIndex = 24;
			this->put->Text = L"Put Option";
			this->put->UseVisualStyleBackColor = true;
			// 
			// call
			// 
			this->call->AutoSize = true;
			this->call->Location = System::Drawing::Point(674, 219);
			this->call->Name = L"call";
			this->call->Size = System::Drawing::Size(185, 31);
			this->call->TabIndex = 23;
			this->call->Text = L"Call Option";
			this->call->UseVisualStyleBackColor = true;
			// 
			// average
			// 
			this->average->Controls->Add(this->time_elapsed);
			this->average->Controls->Add(this->n_avg_prev);
			this->average->Controls->Add(this->n_avg);
			this->average->Controls->Add(this->StAve);
			this->average->Controls->Add(this->label16);
			this->average->Controls->Add(this->label15);
			this->average->Controls->Add(this->label14);
			this->average->Controls->Add(this->label13);
			this->average->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->average->Location = System::Drawing::Point(602, 29);
			this->average->Name = L"average";
			this->average->Size = System::Drawing::Size(307, 172);
			this->average->TabIndex = 22;
			this->average->TabStop = false;
			this->average->Text = L"Average Option";
			// 
			// time_elapsed
			// 
			this->time_elapsed->Location = System::Drawing::Point(219, 130);
			this->time_elapsed->Name = L"time_elapsed";
			this->time_elapsed->Size = System::Drawing::Size(71, 29);
			this->time_elapsed->TabIndex = 33;
			// 
			// n_avg_prev
			// 
			this->n_avg_prev->Location = System::Drawing::Point(219, 95);
			this->n_avg_prev->Name = L"n_avg_prev";
			this->n_avg_prev->Size = System::Drawing::Size(71, 29);
			this->n_avg_prev->TabIndex = 32;
			// 
			// n_avg
			// 
			this->n_avg->Location = System::Drawing::Point(219, 60);
			this->n_avg->Name = L"n_avg";
			this->n_avg->Size = System::Drawing::Size(71, 29);
			this->n_avg->TabIndex = 31;
			// 
			// StAve
			// 
			this->StAve->Location = System::Drawing::Point(219, 25);
			this->StAve->Name = L"StAve";
			this->StAve->Size = System::Drawing::Size(71, 29);
			this->StAve->TabIndex = 30;
			// 
			// label16
			// 
			this->label16->AutoSize = true;
			this->label16->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label16->Location = System::Drawing::Point(6, 135);
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
			this->label15->Location = System::Drawing::Point(6, 100);
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
			this->label14->Location = System::Drawing::Point(6, 65);
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
			this->label13->Location = System::Drawing::Point(6, 30);
			this->label13->Name = L"label13";
			this->label13->Size = System::Drawing::Size(68, 18);
			this->label13->TabIndex = 27;
			this->label13->Text = L"Save,t";
			// 
			// tree
			// 
			this->tree->Controls->Add(this->US);
			this->tree->Controls->Add(this->euro);
			this->tree->Controls->Add(this->layers);
			this->tree->Controls->Add(this->label12);
			this->tree->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->tree->Location = System::Drawing::Point(272, 166);
			this->tree->Name = L"tree";
			this->tree->Size = System::Drawing::Size(306, 122);
			this->tree->TabIndex = 21;
			this->tree->TabStop = false;
			this->tree->Text = L"Tree";
			// 
			// US
			// 
			this->US->AutoSize = true;
			this->US->Location = System::Drawing::Point(167, 74);
			this->US->Name = L"US";
			this->US->Size = System::Drawing::Size(117, 26);
			this->US->TabIndex = 29;
			this->US->Text = L"American";
			this->US->UseVisualStyleBackColor = true;
			// 
			// euro
			// 
			this->euro->AutoSize = true;
			this->euro->Location = System::Drawing::Point(22, 74);
			this->euro->Name = L"euro";
			this->euro->Size = System::Drawing::Size(117, 26);
			this->euro->TabIndex = 28;
			this->euro->Text = L"European";
			this->euro->UseVisualStyleBackColor = true;
			// 
			// layers
			// 
			this->layers->Location = System::Drawing::Point(213, 27);
			this->layers->Name = L"layers";
			this->layers->Size = System::Drawing::Size(71, 29);
			this->layers->TabIndex = 27;
			// 
			// label12
			// 
			this->label12->AutoSize = true;
			this->label12->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label12->Location = System::Drawing::Point(19, 32);
			this->label12->Name = L"label12";
			this->label12->Size = System::Drawing::Size(118, 18);
			this->label12->TabIndex = 27;
			this->label12->Text = L"Tree layers";
			// 
			// lookback
			// 
			this->lookback->Controls->Add(this->n_lookback);
			this->lookback->Controls->Add(this->label11);
			this->lookback->Controls->Add(this->StMax);
			this->lookback->Controls->Add(this->label10);
			this->lookback->Controls->Add(this->StMin);
			this->lookback->Controls->Add(this->label9);
			this->lookback->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->lookback->Location = System::Drawing::Point(272, 29);
			this->lookback->Name = L"lookback";
			this->lookback->Size = System::Drawing::Size(306, 131);
			this->lookback->TabIndex = 20;
			this->lookback->TabStop = false;
			this->lookback->Text = L"Lookback Option";
			// 
			// n_lookback
			// 
			this->n_lookback->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->n_lookback->Location = System::Drawing::Point(213, 92);
			this->n_lookback->Name = L"n_lookback";
			this->n_lookback->Size = System::Drawing::Size(71, 26);
			this->n_lookback->TabIndex = 26;
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
			// StMax
			// 
			this->StMax->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->StMax->Location = System::Drawing::Point(213, 60);
			this->StMax->Name = L"StMax";
			this->StMax->Size = System::Drawing::Size(71, 26);
			this->StMax->TabIndex = 25;
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
			// StMin
			// 
			this->StMin->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->StMin->Location = System::Drawing::Point(213, 28);
			this->StMin->Name = L"StMin";
			this->StMin->Size = System::Drawing::Size(71, 26);
			this->StMin->TabIndex = 24;
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
			// rep
			// 
			this->rep->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->rep->Location = System::Drawing::Point(148, 262);
			this->rep->Name = L"rep";
			this->rep->Size = System::Drawing::Size(71, 26);
			this->rep->TabIndex = 19;
			// 
			// sims
			// 
			this->sims->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->sims->Location = System::Drawing::Point(148, 230);
			this->sims->Name = L"sims";
			this->sims->Size = System::Drawing::Size(71, 26);
			this->sims->TabIndex = 18;
			// 
			// sigma
			// 
			this->sigma->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->sigma->Location = System::Drawing::Point(148, 198);
			this->sigma->Name = L"sigma";
			this->sigma->Size = System::Drawing::Size(71, 26);
			this->sigma->TabIndex = 17;
			// 
			// q
			// 
			this->q->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->q->Location = System::Drawing::Point(148, 166);
			this->q->Name = L"q";
			this->q->Size = System::Drawing::Size(71, 26);
			this->q->TabIndex = 16;
			// 
			// r
			// 
			this->r->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->r->Location = System::Drawing::Point(148, 134);
			this->r->Name = L"r";
			this->r->Size = System::Drawing::Size(71, 26);
			this->r->TabIndex = 15;
			// 
			// T
			// 
			this->T->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->T->Location = System::Drawing::Point(148, 103);
			this->T->Name = L"T";
			this->T->Size = System::Drawing::Size(71, 26);
			this->T->TabIndex = 14;
			// 
			// K
			// 
			this->K->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->K->Location = System::Drawing::Point(148, 71);
			this->K->Name = L"K";
			this->K->Size = System::Drawing::Size(71, 26);
			this->K->TabIndex = 13;
			// 
			// St
			// 
			this->St->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->St->Location = System::Drawing::Point(148, 39);
			this->St->Name = L"St";
			this->St->Size = System::Drawing::Size(71, 26);
			this->St->TabIndex = 12;
			// 
			// label8
			// 
			this->label8->AutoSize = true;
			this->label8->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label8->Location = System::Drawing::Point(16, 264);
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
			this->label7->Location = System::Drawing::Point(16, 232);
			this->label7->Name = L"label7";
			this->label7->Size = System::Drawing::Size(118, 18);
			this->label7->TabIndex = 10;
			this->label7->Text = L"Simulations";
			// 
			// label6
			// 
			this->label6->AutoSize = true;
			this->label6->Font = (gcnew System::Drawing::Font(L"Courier New", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label6->Location = System::Drawing::Point(16, 200);
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
			this->label5->Location = System::Drawing::Point(16, 168);
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
			this->label4->Location = System::Drawing::Point(16, 136);
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
			this->label3->Location = System::Drawing::Point(16, 105);
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
			this->label2->Location = System::Drawing::Point(16, 73);
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
			this->label1->Location = System::Drawing::Point(16, 41);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(108, 18);
			this->label1->TabIndex = 4;
			this->label1->Text = L"Spot Price";
			// 
			// models
			// 
			this->models->Font = (gcnew System::Drawing::Font(L"Courier New", 14.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->models->FormattingEnabled = true;
			this->models->ItemHeight = 21;
			this->models->Items->AddRange(gcnew cli::array< System::Object^  >(5) {
				L"American Option (CRR)", L"European Option (CRR)",
					L"European Option (MC)", L"Lookback European Option (MC)", L"Average European Option (MC)"
			});
			this->models->Location = System::Drawing::Point(308, 32);
			this->models->Name = L"models";
			this->models->Size = System::Drawing::Size(526, 25);
			this->models->TabIndex = 2;
			// 
			// label0
			// 
			this->label0->AutoSize = true;
			this->label0->Font = (gcnew System::Drawing::Font(L"Courier New", 15.75F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label0->Location = System::Drawing::Point(19, 32);
			this->label0->Name = L"label0";
			this->label0->Size = System::Drawing::Size(283, 23);
			this->label0->TabIndex = 3;
			this->label0->Text = L"Choose option type : ";
			// 
			// calc
			// 
			this->calc->Font = (gcnew System::Drawing::Font(L"Courier New", 15.75F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->calc->Location = System::Drawing::Point(683, 371);
			this->calc->Name = L"calc";
			this->calc->Size = System::Drawing::Size(272, 41);
			this->calc->TabIndex = 4;
			this->calc->Text = L"Calculate !";
			this->calc->UseVisualStyleBackColor = true;
			// 
			// mainForm
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 12);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::Menu;
			this->ClientSize = System::Drawing::Size(984, 761);
			this->Controls->Add(this->calc);
			this->Controls->Add(this->label0);
			this->Controls->Add(this->models);
			this->Controls->Add(this->inputBox);
			this->Controls->Add(this->outputBox);
			this->MaximumSize = System::Drawing::Size(1000, 800);
			this->MinimumSize = System::Drawing::Size(1000, 800);
			this->Name = L"mainForm";
			this->Text = L"Option Price Calculator";
			this->outputBox->ResumeLayout(false);
			this->outputBox->PerformLayout();
			this->inputBox->ResumeLayout(false);
			this->inputBox->PerformLayout();
			this->average->ResumeLayout(false);
			this->average->PerformLayout();
			this->tree->ResumeLayout(false);
			this->tree->PerformLayout();
			this->lookback->ResumeLayout(false);
			this->lookback->PerformLayout();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	};
}
